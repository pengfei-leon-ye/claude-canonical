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

At review the advisor also reports each sleeve's **A/H venue mix** (A股 vs 港股), derived from each holding's ticker — the §9.4 listing-venue diagnostic. It is a *graded* risk-tiering input, **not** a hard quota and **not** a stored field; flag a deliberate A/H lean only as a §1.2 flip-condition judgment, never a fixed ratio.

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

## Human-capital context (人力资本背景 — §9.3)

Human capital — the present value of future earnings — is the investor's largest asset for most life stages and is **invisible in a brokerage snapshot**. The advisor cannot infer it from holdings, so it is carried here as a **known input** (framework §9.3 / Invariant 10). It drives the employer/sector **underweight**: total economic exposure = financial position + human capital, and the two are positively correlated.

| Field | Value (private copy only) | Used for |
|---|---|---|
| Employer (雇主) + listed & holdable? | ____ | Whether the employer's stock is a correlated double-exposure |
| Career sector(s) (职业所在行业) | ____ | Add no satellite theme here (§9.3) |
| Employer-stock holding (雇主股票) | shares / cost / RSU-vested vs open-market | Hold well below the per-position cap regardless of thesis; also listed in Holdings above |
| Equity-vesting pipeline (待归属股权) | approx. schedule & size | Re-adds exposure over time → standing trim-as-vested policy |

_Blank in this canonical schema; fill only in the private copy. If the investor has no employer/sector concentration, record "n/a" — do not omit the assessment (§9.3 requires it be assessed separately, not inferred from holdings)._
