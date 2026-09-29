# -*- coding: utf-8 -*-
"""
同花顺实盘高速量化网关 - Python SDK 客户端 (Zero-Dependency)
纯 Python 标准库编写，零 pip 依赖，开箱即用。
"""

import json
from typing import Any, Dict, List, Optional
import urllib.error
import urllib.parse
import urllib.request


class ShipanClient:
    """同花顺本地实盘网关客户端"""

    def __init__(self, host: str = "127.0.0.1", port: int = 19312, timeout: float = 3.0):
        self.base_url = f"http://{host}:{port}"
        self.timeout = timeout

    def _request(self, method: str, path: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        headers = {"Content-Type": "application/json"}
        req_data = None
        if data is not None:
            req_data = json.dumps(data, ensure_ascii=False).encode("utf-8")

        req = urllib.request.Request(url, data=req_data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                content = response.read().decode("utf-8")
                return json.loads(content)
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            try:
                return json.loads(err_body)
            except Exception:
                return {"ok": False, "error": f"http_{e.code}", "message": str(e)}
        except urllib.error.URLError as e:
            return {
                "ok": False,
                "error": "connection_failed",
                "message": f"无法连接到同花顺本地网关 ({self.base_url})，请确认网关程序是否已启动: {e.reason}",
            }
        except Exception as e:
            return {"ok": False, "error": "unknown_exception", "message": str(e)}

    # ==================== 状态检查 ====================

    def health(self) -> Dict[str, Any]:
        """获取网关健康状态、授权信息及同花顺连接状态"""
        return self._request("GET", "/v1/health")

    # ==================== 核心交易接口 ====================

    def buy(self, symbol: str, price: float, amount: int) -> Dict[str, Any]:
        """买入股票 / ETF
        :param symbol: 6位证券代码，如 '000001', '600519', '159915'
        :param price: 委托价格 (元)
        :param amount: 委托股数 (整百股，如 100)
        """
        payload = {"symbol": str(symbol).strip(), "price": float(price), "amount": int(amount)}
        return self._request("POST", "/v1/buy", payload)

    def sell(self, symbol: str, price: float, amount: int) -> Dict[str, Any]:
        """卖出股票 / ETF
        :param symbol: 6位证券代码，如 '000001', '600519', '159915'
        :param price: 委托价格 (元)
        :param amount: 委托股数 (整百股，如 100)
        """
        payload = {"symbol": str(symbol).strip(), "price": float(price), "amount": int(amount)}
        return self._request("POST", "/v1/sell", payload)

    def cancel(self, entrust_no: str) -> Dict[str, Any]:
        """撤单
        :param entrust_no: 委托合同编号 (字符串)
        """
        payload = {"entrust_no": str(entrust_no).strip()}
        return self._request("POST", "/v1/cancel", payload)

    # ==================== 核心查询接口 ====================

    def get_balance(self) -> Dict[str, Any]:
        """查询资金资产 (总资产、可用资金、总市值等)"""
        return self._request("GET", "/v1/balance")

    def get_positions(self) -> Dict[str, Any]:
        """查询当前持仓明细 (股票代码、持仓数量、可用数量、参考市值等)"""
        return self._request("GET", "/v1/positions")

    def get_entrusts(self) -> Dict[str, Any]:
        """查询当日委托明细"""
        return self._request("GET", "/v1/entrusts")

    def get_deals(self) -> Dict[str, Any]:
        """查询当日成交明细"""
        return self._request("GET", "/v1/deals")
