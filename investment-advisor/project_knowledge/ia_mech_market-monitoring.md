# Market Monitoring Rubric (Gray-Rhino Watch)

**Consumption model.** Loaded as project knowledge, and intended to be the rubric a scheduled monitoring routine (a future, separate deliverable) executes. Carries zero personal data. Pairs with `ia_os_investment-strategy-framework.md` — alerts here map to actions there. This is the **macro sensor**; deriving the single-name entry/exit price zone for an already-approved action is the separate job of `ia_mech_technical-analysis.md`.

## 1. Purpose and honest scope

This system does **not** predict black swans. By definition (Taleb) a true black swan is unforecastable; the structural defense against it is the **hedge sleeve** (framework §4), not news reading [通识]. What this rubric *can* do:

- **Gray-rhino early warning** (Wucker) — high-probability, high-impact, *ignored* risks are trackable; surface them before they hit [通识].
- **Faster reaction** — once an event is underway, compress the time from "it started" to "the investor has a considered response."

Set expectations accordingly: the deliverable is earlier awareness and disciplined reaction, not prophecy. A quiet day is a valid output.

## 2. Watchlist — five categories

Scan these; weight toward whatever touches the portfolio's actual sector exposure (read from the holdings data file at runtime).

1. **Policy / regulatory** — 十五五 execution and shifts; sector-specific regulation affecting holdings; monetary policy (PBoC rates, liquidity); fiscal stance; capital-market rules (沪港通/港股通 access, listing rules for 科创板/创业板).
2. **Geopolitics / 风向** — 中美关系, technology export controls and entity lists, tariffs, sanctions; 台海; anything shifting the 自主可控 / 国产替代 thesis.
3. **Macro data** — PMI, CPI/PPI, 社融/credit, GDP prints, CNY exchange rate, 北向资金 flows.
4. **Market structure / holdings** — sector prosperity (景气度) of held themes; leaders' earnings pre-announcements (业绩预告); industry-chain price signals (上下游 prices); valuation-percentile extremes in held names.
5. **Global** — US Fed path and US Treasury yields, global risk-off signals, major commodities (esp. those upstream of held themes), gold.

## 3. Severity and escalation tiers

Rate each finding; only Tier 2+ reaches the investor as an alert. Tier 1 accumulates into the routine digest.

- **Tier 1 — Note.** Relevant but not action-changing. Goes in the digest, no push.
- **Tier 2 — Watch.** Could affect a thesis or allocation if it develops. Push a concise alert; link to the framework review clock it implicates (usually quarterly thesis review or the annual strategic review).
- **Tier 3 — Act-candidate.** Materially threatens a holding's thesis, breaches or approaches a rebalancing band, or hits a stated **flip condition** of the China-overweight bet (framework §1.2). Push immediately with a recommended action *derived from the framework* (e.g., "thesis review on X now," "hedge sleeve toward 15%," "risk sleeve approaching 65% ceiling").

Escalation bias: a developing situation that is *ambiguous but high-impact* should escalate one tier higher than its current certainty suggests — the cost of an early heads-up is low; the cost of a late one is the whole point of the system.

## 4. Output format

Each run produces a digest:

1. **Headline** — one line: overall posture (calm / watch / act) and the single most important item.
2. **By category** — only categories with Tier 1+ findings; each finding = what happened · why it matters to *this* portfolio · severity tier · source (with recency/authority).
3. **Action items** — Tier 2/3 only, each mapped to a framework action and review clock. None is a valid, good output.
4. **Open threads** — situations being tracked across runs, with what would escalate them.

Every factual claim carries a source and recency; never assert market/regulatory specifics from memory.

## 5. Cadence

- **Daily light scan** — fast pass over the watchlist; emit the digest; push only on Tier 2+.
- **Event-driven** — a Tier 3 finding pushes immediately, off-cadence.
- Tune frequency to regime: calmer markets tolerate a lighter touch; elevated stress (or an open Tier 2 thread) warrants closer watch.

## 6. Linkage to framework actions

Monitoring is the *sensor*; the framework is the *controller*. The rubric never invents trades — it routes findings to the framework's existing machinery:

- Thesis-threatening news → **quarterly fundamental review** (framework §7), possibly pulled forward → §6.6 broken-thesis exit if confirmed.
- Allocation drift / volatility spike → **rebalancing bands** (§8); the counter-cyclical hedge reflex (§4) is the default response to a China-wide sell-off, executed by rule, not panic.
- Macro/geopolitical regime shift → **annual strategic review** and the China-bet **flip conditions** (§1.2).

## 7. Note on the scheduled routine

The automated routine that executes this rubric (periodic search → interpret → severity-rate → push) is a **separate, optional deliverable** to be built after this rubric is reviewed. It will consume this file as its instruction set; keeping the rubric well-specified here is what makes the routine's alerts trustworthy. The routine reads portfolio sector exposure from the private data files at runtime; it writes no personal data back into this repo.
