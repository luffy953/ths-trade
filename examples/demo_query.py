# -*- coding: utf-8 -*-
"""
同花顺实盘高速量化网关 - 资产、持仓与当日委托查询示例
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sdk.shipan import ShipanClient


def main():
    print("=" * 65)
    print("        同花顺实盘高速网关 - 核心查询演示 (资金/持仓/委托)     ")
    print("=" * 65)

    client = ShipanClient(host="127.0.0.1", port=19312)

    # 1. 资金资产查询
    print("📊 查询账户资金状况 (POST /v1/balance)...")
    balance = client.get_balance()
    print(f"   返回结果: {balance}")

    # 2. 持仓股票查询
    print("\n📊 查询持仓明细 (POST /v1/positions)...")
    positions = client.get_positions()
    print(f"   返回结果: {positions}")

    # 3. 当日委托查询
    print("\n📊 查询当日委托记录 (POST /v1/entrusts)...")
    entrusts = client.get_entrusts()
    print(f"   返回结果: {entrusts}")
    print("=" * 65)


if __name__ == "__main__":
    main()
