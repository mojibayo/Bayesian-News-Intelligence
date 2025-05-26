# CryseraOne — Real-Time Macroeconomic News Impact Analyzer

> This is the starting point for a much bigger project I’m working on. It tracks breaking macro and financial news, pulls out the important parts, and analyzes their potential market impact. The system then runs that analysis through a Bayesian framework to estimate how likely it is to move the market.

> It can be used to support risk analysis, guide market calls, or even feed into more advanced tools like VAR models. It’s still early, but the foundation is solid and there’s a lot of room to build on.

## 🚀 What It Does

- **Real-Time Macro News Monitoring**  
  Tracks breaking business and economic news using GNews API (or any news source you plug in).

- **Relevance Detection**  
  Filters for key macroeconomic events using custom-built keyword logic.

- **AI-Powered Impact Analysis**  
  Uses GPT-4 to assess how the event might affect major assets (USD, EUR, Gold, JPY, Bitcoin), including:
  - Sentiment (bullish/bearish/neutral)
  - Confidence score (0.00–1.00)
  - Market bias
  - Marginal likelihood of impact
  - Hypothesized outcome

- **Bayesian Posterior Calculation**  
  Computes updated belief about market impact based on confidence and prior probability.

- **Formatted JSON Outputs**  
  For easy parsing into dashboards, alert systems, or further quant processing.

---

## 🧠 Why It's Useful

### For Risk Analysts & Hedge Fund Strategists

- **Event-Driven VaR & Stress Testing**  
  Plug impact scores and Bayesian posterior into a VAR model as a forward-looking macro input.

- **Pre-Trade Sentiment Scoring**  
  Generate sentiment vectors per asset ahead of trades or rebalancing decisions.

- **Crisis Monitoring**  
  Quickly gauge global bias (risk-on/off) when central banks, oil producers, or governments speak.

- **Risk Alerts & Communication**  
  Feed JSON output into a Slack or Discord bot to alert the team in real-time.

- **Macro Narrative Building**  
  Build context-rich macro decks or internal memos using AI-generated reasoning and hypotheses.

---

## 🧩 Example Output

```json
{
  "headline": "Masayoshi Son floats idea of US-Japan sovereign wealth fund",
  "impact_summary": "The proposal... could strengthen both currencies and raise oil prices.",
  "bias": "bullish",
  "confidence": 0.75,
  "posterior": 0.80
}
```

This tells you:
- Markets may lean bullish short-term.
- USD, JPY could strengthen.
- Consider adjusting portfolio risk or currency exposure.
- Posterior probability (0.80) indicates high belief in impact.

---

## 🛠 Integration Ideas

- Feed into a VAR model as an external shock input.
- Use CryseraOne outputs as feature signals for macro trading algos.
- Auto-generate reports for your Chief Risk Officer or investment committee.
- Combine with Bloomberg or Refinitiv alerts for deeper narrative context.

---

## ⚙️ Technologies Used

- OpenAI GPT-4
- Bayesian Inference
- GNews API
- Python 3.11+

---

`CryseraOne provides AI-generated probabilistic insight, not investment advice.`

- vythea ✷
