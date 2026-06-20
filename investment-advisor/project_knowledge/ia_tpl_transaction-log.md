# Transaction Log — Schema / Template

**Canonical schema (the blank `.env.example`) for the Investment Advisor's transaction-log runtime data.** Carries zero real data — only field definitions and illustrative examples. To use: copy this into the private `investment-advisor-private/` folder, delete the examples, and append real trades; upload **only the filled copy** to claude.ai project knowledge. Never enter real trades into this canonical copy.

Append a row on **every** trade. The advisor uses the filled log for the net-long invariant check (持有时间 > 不持有时间), cost-basis evolution (chip accumulation), and a behavior audit (did the trade follow the method, or was it a chase/panic?). Append-only — never delete or rewrite history; append corrections as new rows.

**Action vocabulary:** **Buy** = establish initial 底仓 (value-based) · **Add** = buy-back-low (cheap leg of the cycle) · **Trim** = partial sell-high (expensive leg) · **Sell** = full exit (usually a broken thesis). Moves are partial (~1/3); never all-in / all-out.

**Rationale** must capture: **valuation zone** (cheap/expensive, ideally a percentile) · the **trigger** (valuation primary + optional secondary-trend confirmation) · **thesis status**. This is what makes the log auditable against the framework.

| 日期 Date | 名称/代码 Name | Sleeve | 动作 Action | 股数 Shares | 价格 Price | 金额 Amount | 理由 Rationale (估值区间 + 触发 + 逻辑) | 操作后 Post (股数 / 成本均价) |
|---|---|---|---|---|---|---|---|---|
| _2026-01-15 (example)_ | 示例-科技成长股A | Risk | Buy | 1500 | 40.00 | 60,000 | 估值~25分位(低)；建底仓；逻辑 Intact | 1500 / 40.00 |
| _2026-03-20 (example)_ | 示例-科技成长股A | Risk | Add | 500 | 35.00 | 17,500 | 中期回调至~15分位；逻辑未变；买回更便宜 | 2000 / 38.75 |
| _2026-05-10 (example)_ | 示例-周期标的B | Risk | Trim | 1000 | 18.00 | 18,000 | 估值~80分位(高) + 中期趋势转弱确认；减1/3 | 2000 / 12.00 |

_The rows above are illustrative; the filled private copy replaces them with real trades._ The two example-A rows show the chip effect: buying the cheap leg pulled cost/share from 40.00 → 38.75 while raising the share count.
