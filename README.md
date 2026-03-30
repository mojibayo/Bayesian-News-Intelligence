# CryseraOne

**Real-Time Macroeconomic News Impact Analyzer**

AI-powered system that tracks breaking macro news, extracts key signals, and quantifies their likely market impact using GPT-4 + Bayesian inference.

Built as the foundation for advanced macro trading, risk, and quant workflows.

---

## Features

- **Live News Monitoring** — Pulls breaking business & economic headlines (GNews or any source)
- **Smart Relevance Filter** — Detects true macro events with custom keyword logic
- **AI Impact Analysis** — GPT-4 scores sentiment, confidence (0–1), market bias, and hypothesized outcomes across USD, EUR, Gold, JPY, Bitcoin
- **Bayesian Posterior** — Updates probability of market move in real time
- **Clean JSON Output** — Ready for dashboards, alerts, VAR models, or algos

---

## Example Output

```json
{
  "headline": "Masayoshi Son floats idea of US-Japan sovereign wealth fund",
  "impact_summary": "Proposal could strengthen USD and JPY while lifting oil prices",
  "assets_affected": ["USD", "JPY", "Oil"],
  "bias": "bullish",
  "confidence": 0.75,
  "posterior": 0.80
}
```

---

## Why It Matters

- Pre-trade macro sentiment scoring
- Real-time risk alerts & VaR stress inputs
- Event-driven portfolio adjustments
- Crisis monitoring and narrative building
- Direct feed into quant models or Slack/Discord bots

