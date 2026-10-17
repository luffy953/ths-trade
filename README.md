# ⚡ 同花顺/通达信实盘高速量化交易网关 (THS Native Trade Gateway)

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%207%2F10%2F11%2FServer-0078D6.svg?logo=windows)](https://github.com/luffy953/ths-trade)
[![Language](https://img.shields.io/badge/Language-Python%20%7C%20REST%20API-3776AB.svg?logo=python)](https://github.com/luffy953/ths-trade)
[![Latency](https://img.shields.io/badge/Execution%20Latency-%3C%205ms-brightgreen.svg)]()
[![Brokers](https://img.shields.io/badge/Brokers-100%2B%20Supported-orange.svg)]()

**专为专业量化团队与个人交易员打造的高性能、全后台、非 UI 模拟的同花顺实盘穿透交易网关**  
*毫秒级极速执行 · 纯后台内存级通信 · 不抢占鼠标键盘 · 百家券商通用 · 零环境依赖*

[🚀 核心优势](#-核心优势) • [📊 方案对比](#-技术方案对比) • [💻 快速上手](#-快速上手) • [📖 接口规范](#-restful-api-规范) • [💬 免费试用与交流](#-免费试用与技术交流)

</div>

---

## 📌 为什么需要本项目？

在 A 股做量化实盘，交易员与机构长期受困于两大痛点：

1. **官方机构接口门槛极高**：券商官方 QMT / PTrade / CTP 往往要求 **50 万 ~ 500 万** 的资金门槛，审核流程漫长，且很多中小券商根本不提供；
2. **传统开源 UI 方案极不稳定**：市面上常见的自动化工具（如基于 `PyAutoGUI`、`Win32 API` 模拟按键、易语言找图找色）本质上是**屏幕点击模拟**：
   - 🐢 **延迟奇高**：模拟找图、点击、剪贴板粘贴，一笔委托耗时动辄 **500ms ~ 2000ms**，严重错失买卖点；
   - 💥 **极易崩溃**：交易时必须**独占屏幕**，前台稍有弹窗、鼠标碰一下、屏幕锁屏或分辨率缩放，就会导致**点错买卖、废单甚至重复下单**；
   - 🤯 **无法多开**：一台电脑只能前台操作一个账号，无法满足多策略、多券商分仓并发交易需求。

**本项目通过彻底颠覆传统的“点屏幕”逻辑，采用纯非 UI 的底层活跃 IPC 穿透技术，为您提供亚毫秒级的实盘交易执行体验。**

---

## 🚀 核心优势

- ⚡ **亚毫秒级极致延迟**：底层通信穿透耗时 **`< 5ms`**（通常在 1~3ms），比传统点屏幕方案快 **100 倍以上**，打板抢筹、条件单触发快人一步。
- 🖥️ **纯后台静默运行（非 UI 自动化）**：
  - **不抢鼠标、不占键盘、不依赖屏幕分辨率**；
  - 同花顺客户端可以最小化在后台静默运行，前台写代码、看盘、浏览网页完全不受干扰，彻底告别误触。
- 🏦 **全券商通用生态**：
  - 基于同花顺标准核心开发，支持全国 **100+ 主流券商**（中信证券、国泰君安、银河证券、华泰证券、广发证券、招商证券、申万宏源、海通证券等）；
  - 无需特定券商开通量化白名单，只要您的同花顺能登录，就能立即自动交易。
- 🎯 **全市场品种支持**：
  - 支持 **主板、创业板、科创板、北交所** 股票交易；
  - 完美支持 **沪深全市场 ETF**（`159`、`51`、`58` 等基金代码自动智能路由匹配对应股东账号）；
  - 支持 **可转债** 高频买卖与快速撤单。
- 📦 **零环境依赖，开箱即用**：
  - 独立绿色单文件 Windows 服务，客户电脑**无需安装 Python、无需配置 C++ 运行库或任何依赖包**；
  - 本地提供标准 **RESTful HTTP API**，策略端支持 Python、C++、Go、NodeJS、Java、C# 或任意量化框架接入。
- 🔄 **单机多开与并发支持**：
  - 支持多实例多端口独立运行（如 `19312`、`19313`、`19314`），单台电脑可同时挂接多个券商资金账号，多账户并发下单、互不干扰。

---

## 📊 技术方案对比

| 对比维度 | 传统 UI 模拟方案 (PyAutoGUI / 易语言) | 券商官方接口 (QMT / PTrade) | **本项目 (THS Native Gateway)** |
| :--- | :--- | :--- | :--- |
| **底层实现机制** | 前台截屏、找图、模拟鼠标点击输入 | 券商私有 C++ / Python SDK | **底层活跃 IPC / 套接字穿透通信** |
| **指令执行延迟** | **500ms ~ 2000ms** (极慢) | 10ms ~ 50ms | **< 5ms (极速，通常 1~3ms)** |
| **屏幕独占要求** | **必须独占**（不能动鼠标、不能锁屏） | 无需独占 | **完全后台静默，可最小化** |
| **资金准入门槛** | 无门槛 | **50万 ~ 500万** (门槛高且需审批) | **零门槛，任意普通资金账号均可** |
| **券商覆盖范围** | 仅限适配过的特定版面 | 仅限已开通的单家券商 | **100+ 家主流券商全通用** |
| **多账户多开** | ❌ 无法多开（鼠标只有一个） | 视券商版本而定 | **✅ 完美支持单机多端口多账号并发** |
| **环境依赖** | 复杂 Python 环境、图像识别库 | 限制 Python 3.6/3.7，依赖专用客户端 | **✅ 零依赖绿色 EXE，双击即跑** |


---

## 💻 快速上手

### 1. 启动网关
1. 电脑打开同花顺客户端并登录资金账号；
2. 双击运行 `shipan-gateway.exe`（自动在本地 `127.0.0.1:19312` 开启高速监听服务）。

### 2. Python 策略端调用 (使用本项目内置轻量 SDK)

本项目提供纯标准库实现的 Python 客户端 SDK（位于 `sdk/shipan.py`，**零 pip 依赖**）：

```python
from sdk.shipan import ShipanClient

# 初始化客户端 (默认连接本地 19312 网关)
client = ShipanClient(host="127.0.0.1", port=19312)

# 1. 检查网关与实盘连接状态
status = client.health()
print(f"网关连接状态: {status}")

# 2. 极速买入股票 (平安银行 100 股，价格 9.50)
res_buy = client.buy(symbol="000001", price=9.50, amount=100)
print(f"买入报单成功: 耗时 {res_buy.get('elapsedMs')} ms")

# 3. 极速卖出股票 (平安银行 100 股，价格 15.00)
res_sell = client.sell(symbol="000001", price=15.00, amount=100)
print(f"卖出报单成功: 耗时 {res_sell.get('elapsedMs')} ms")

# 4. 委托撤单 (指定合同编号)
res_cancel = client.cancel(entrust_no="123456")
print(f"撤单结果: {res_cancel}")

# 5. 查询账户资金与持仓
balance = client.get_balance()      # 查可用资金、总资产
positions = client.get_positions()  # 查持仓股票与可用股数
entrusts = client.get_entrusts()    # 查当日委托列表
```

---

## 📖 RESTful API 规范

任何编程语言（C++、Go、Java、Node.js、Rust 等）或命令行工具均可直接向本地网关发送标准 HTTP 请求：

### 1. 健康与就绪检查
- **接口**：`GET /v1/health`
- **响应示例**：
```json
{
  "ok": true,
  "service": "shipan_ths_gateway",
  "version": "1.0.0",
  "connected": true,
  "account": "8886381233",
  "license": {
    "ok": true,
    "expire_date": "2026-10-29 23:59:59",
    "remaining_days": 2
  }
}
```

### 2. 股票 / ETF 买入
- **接口**：`POST /v1/buy`
- **请求体**：
```json
{
  "symbol": "000001",
  "price": 9.50,
  "amount": 100
}
```
- **响应示例**：
```json
{
  "ok": true,
  "elapsedMs": 2.14,
  "symbol": "000001",
  "price": 9.5,
  "amount": 100
}
```

### 3. 股票 / ETF 卖出
- **接口**：`POST /v1/sell`
- **请求体**：
```json
{
  "symbol": "600519",
  "price": 1800.00,
  "amount": 100
}
```

### 4. 委托撤单
- **接口**：`POST /v1/cancel`
- **请求体**：
```json
{
  "entrust_no": "987654321"
}
```

### 5. cURL 命令行快速测试
```bash
curl -X POST http://127.0.0.1:19312/v1/buy \
     -H "Content-Type: application/json" \
     -d '{"symbol": "000001", "price": 9.50, "amount": 100}'
```

---

## ❓ 常见问题 (FAQ)

<details>
<summary><b>Q1: 使用本网关有被券商风控或封号的风险吗？</b></summary>

> **完全合规安全**。  
> 本网关与市面上篡改券商通信协议的非法外挂有本质区别：网关只运行在您自己的本地电脑上，通过同花顺合法的本地活跃套接字与同花顺交互，最终所有报文均由同花顺官方客户端完成合法身份签名并发送至券商。在券商柜台眼中，所有委托都是来自**官方同花顺客户端的正常委托**，零风控异常。
</details>

<details>
<summary><b>Q2: 我的同花顺安装在 D 盘或其他路径，能自动识别吗？</b></summary>

> **百分之百自适应**。  
> 网关采用操作系统级进程动态枚举（PID 枚举与本地套接字自动嗅探），不管您将同花顺安装在 C 盘、D 盘、E 盘还是任意深度自定义路径，只要同花顺进程运行并登录，网关会在 **0.1 毫秒** 内自动完成发现与握手，绝无路径硬编码。
</details>

<details>
<summary><b>Q3: 我有多个不同的券商账户，可以在同一台电脑上同时跑吗？</b></summary>

> **支持单机多开**。  
> 您只需将网关复制出多份文件夹（如 `gateway-1/`、`gateway-2/`），在各自的 `config.json` 中配置不同的端口（如 `19312`、`19313`）以及对应券商账号。策略程序分别向不同端口发送请求，即可实现多个资金账户的完全并行独立交易。
</details>

<details>
<summary><b>Q4: 我的策略跑在 Linux 云服务器上，如何使用该网关？</b></summary>

> 同花顺客户端仅支持 Windows 平台。通常量化团队的推荐架构为：在本地 Windows 电脑（或 Windows 云主机）挂载同花顺与本网关作为**独立执行节点（Sidecar）**；Linux 策略端通过内网 HTTP API 跨机器调用 Windows 节点，实现“策略算力与实盘执行分离”。
</details>

---

## 💬 免费试用与技术交流

我们为广大量化交易员、私募团队和个人开发者提供 **通用免费试用版本（开箱即用，无需配置环境）**，欢迎添加微信体验交流：

<div align="center">

<img src="assets/wechat_qrcode.jpg" alt="微信联系名片 1 (luffy953)" width="210" style="border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.15); margin: 0 10px;"/>
&nbsp;&nbsp;
<img src="assets/wechat_qrcode2.jpg" alt="微信联系名片 2 (LUFFY9531)" width="210" style="border-radius: 8px; border: 1px solid rgba(255,255,255,0.15); box-shadow: 0 4px 16px rgba(0,0,0,0.15); margin: 0 10px;"/>

### 📱 微信 1：**`luffy953`** &nbsp;&nbsp;&nbsp;&nbsp; 📱 微信 2：**`LUFFY9531`**  
*(添加时请备注：**GitHub / 实盘**，若某个号添加频繁请尝试另一个，以便优先通过)*

</div>

### 🤝 我们还可以为您提供：
- 🎯 **免费试用安装包获取**：解压即用，2 天全功能无限制实操体验真实交易链路；
- ⚡ **Level-2 高频数据接入**：千档买卖盘口、逐笔成交、逐笔委托毫秒级数据通道；
- 📈 **量化实盘系统全套建设**：从高频行情接入、异动抢筹/打板策略，到极速穿透执行与多账户风控管理全链路私有化定制。

---

## ⚠️ 免责声明 (Disclaimer)

1. 本项目所提供的文档、SDK 及代码示例仅用于**量化策略研发、软件工程架构与学术技术交流**。
2. 任何人因使用本项目产生的任何直接或间接投资损失，本项目作者及贡献者概不承担任何责任。
3. 证券市场有风险，投资决策需谨慎。请使用者严格遵守中国证监会及相关证券法规。
