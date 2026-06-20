# Portfolio State — Schema / Template

**Canonical schema (the blank `.env.example`) for the Investment Advisor's portfolio-state runtime data.** Carries zero real data — only field definitions and illustrative examples. To use: copy this into the private `investment-advisor-private/` folder, delete the examples, enter real positions, and upload **only the filled copy** to claude.ai project knowledge. Never enter real positions/capital into this canonical copy. The advisor reads the *filled instance* per Investment Strategy Framework §10; you maintain **shares + cost basis + thesis status**, and the advisor fills **current price / market value / current %** at review (via web lookup, never memory). Refresh the filled snapshot at each monthly (light) and quarterly (deep) review.

## Snapshot metadata

- **As-of date (快照日期):** YYYY-MM-DD
- **Total invested capital (已投本金):** ____
- **Available cash (可用现金):** ____
- **Capital tier (资金档位):** small / medium / large  — per §9.1

## Sleeve allocation (目标 vs 当前)

Target: **Stable 45% / Risk 45% / Hedge 10%** (hedge may flex to 15%). Inter-sleeve rebalance band **±7–10pp**; hard ceiling **Risk ≤ 65%**. The advisor computes current % from the holdings below at review.

| Sleeve | Target | Current (advisor fills) | Within band? |
|---|---|---|---|
| Stable (core) | 45% | | |
| Risk (satellite) | 45% | | |
| Hedge | 10% | | |

## Holdings

**Tier** (risk sleeve only): **Compounder** = low trim-intensity (hold; trim only at extreme valuation) · **Cyclical** = high trim-intensity (the 先卖再买 cycle arena).
**Thesis** status: **Intact / Watch / Broken** — Broken → exit per §6.6, regardless of chip count.
Per-position guardrails (§9.2): single risk position ≤ ~15% of risk sleeve (~8% of total), ≥ ~2–3% floor.

| 名称/代码 Name | Sleeve | Theme (risk) | Tier (risk) | 股数 Shares | 成本均价 Cost/sh | 逻辑状态 Thesis | 备注 Notes |
|---|---|---|---|---|---|---|---|
| _示例-宽基ETF (example)_ | Stable | — | — | 10000 | 3.85 | Intact | 沪深300 / 中证A500 类 |
| _示例-红利低波ETF (example)_ | Stable | — | — | 8000 | 1.02 | Intact | 防御 / 现金流锚 |
| _示例-黄金ETF (example)_ | Hedge | — | — | 5000 | 4.50 | Intact | 尾部保险，非收益来源 |
| _示例-科技成长股A (example)_ | Risk | 自主可控 / 半导体 | Compounder | 2000 | 38.75 | Intact | 让利润奔跑，极端高估才小减 |
| _示例-周期标的B (example)_ | Risk | 新能源 / 储能 | Cyclical | 2000 | 12.00 | Watch | 先卖再买主战场 |

_The rows above are illustrative; the filled private copy replaces them with real holdings._
