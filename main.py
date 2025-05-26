import os
import time
import requests
import openai
from datetime import datetime
from typing import List
import sys
import json


openaikey = "openai api key goes here"
gnewskey = "gnews api key goes here"

assets = ['USD', 'EUR', 'JPY', 'Bitcoin', 'Gold']
keywords = [
    "FOMC", "Powell", "interest rate", "inflation", "ECB", "CPI", "PPI", "debt ceiling",
    "monetary policy", "central bank", "rate hike", "quantitative easing", "GDP", "unemployment",
    "tariff", "oil production", "OPEC", "Fed", "Federal Reserve", "Trump",
]

openai.api_key = openaikey

def isrelevant(text: str) -> bool:
    text_lower = text.lower()
    return any(keyword.lower() in text_lower for keyword in keywords)

def analyze_rep(headline: str, summary: str) -> str:
    system_prompt = """
You are CryseraOne, the smartest, most intelligent and advanced elite AI forex and macroeconomic analyst.

Your task is to assess the impact of breaking news headlines on global assets. Based on the input headline and summary, generate:
- Determine the confidence (0.00 to 1.00) that the news will significantly impact markets.
- Evaluate the sentiment direction (bullish, bearish, neutral) for each core asset.
- Generate a brief but insightful impact summary.
- Provide clear reasoning for your assessment.
- Suggest the primary commodity or asset to monitor.
- Output the overall market bias inferred from the event.
- What you think is going to happpen in a short, ,sharp, summarized, concise and straight forward manner. Based on your conviction, sentiment, confidence and bias. It should describe the most probable market outcome.
- The marginal probability or rather say likelihood of the event happening in the market regardless of market conditions and all biases (0.00 to 1.00). Independent of any hypothesis. Make it extremely accurate and precise.

Format your output strictly in JSON:

{
  "headline": "...",
  "impact_summary": "...",
  "impacted_assets": {
    "USD": "bullish/bearish/neutral",
    "EUR": "bullish/bearish/neutral",
    "Gold": "bullish/bearish/neutral",
    "Bitcoin": "bullish/bearish/neutral",
    "JPY": "bullish/bearish/neutral"
  },
  "bias": "bullish/bearish/neutral",
  "confidence": "...",
  "reasoning": "...",
  "primary_commodity": "...",
  "hypothesis":  "...",
  "marginal": "..."
}
"""
    user_prompt = f"Headlines: {headline}\nSummary: {summary}"
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt.strip()},
                {"role": "user", "content": user_prompt.strip()}
            ],
            temperature=0.4,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI API call failed — {e}")
        return

def process(json_analysis: dict, article_url: str):
    headline = json_analysis.get("headline", "no headline")
    impact_summary = json_analysis.get("impact_summary", "no impact summary")
    impacted_assets = json_analysis.get("impacted_assets", "no impacted asset")
    bias = json_analysis.get("bias", "no bias")
    confidence = json_analysis.get("confidence", "no confidence")
    reasoning = json_analysis.get("reasoning", "no reasoning")
    primary_commodity = json_analysis.get("primary_commodity", "no primary commodity")
    hypothesis = json_analysis.get("hypothesis", "no hypothesis")
    marginal = json_analysis.get("marginal", "no marginal")


    try:
        confidence = float(confidence)
    except (ValueError, TypeError):
        confidence = 0.5

    if bias == "bullish":
        likelihood = (confidence, 1 - confidence)
    elif bias == "bearish":
        likelihood = (1 - confidence, confidence)
    else:
        likelihood = (0.5, 0.5)

    return {
        "headline": headline,
        "impact_summary": impact_summary,
        "impacted_assets": impacted_assets,
        "bias": bias,
        "confidence": confidence,
        "reasoning": reasoning,
        "primary_commodity": primary_commodity,
        "hypothesis": hypothesis,
        "likelihood": likelihood,
        "marginal": marginal
    }

def bayesian(theoryval):
    pe = theoryval["likelihood"][0]
    h = theoryval["confidence"]
    m = theoryval.get("marginal", 0.5)

    try:
        m = float(m)
    except Exception:
        m = 0.5

    if m == 0:
        return 0

    posterior = (pe * h) / m
    return posterior

def news() -> List[dict]:
    url = f"https://gnews.io/api/v4/top-headlines?token={gnewskey}&topic=business&lang=en&max=10"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.json().get("articles", [])
        else:
            print(f"GNews API call error {res.status_code}: {res.text}")
            return []
    except Exception as e:
        print(f"GNews fetch error: {e}")
        return []
    
def main():
    print("CryseraOne")
    seen_urls = set()

    while True:
        articles = news()
        for article in articles:
            url = article.get("url", "")
            if url in seen_urls:
                continue
            seen_urls.add(url)

            headline = article.get("title" , "")
            summary = article.get("description", "")

            print(f"Analyzing {headline}...")

            if isrelevant(f"{headline} {summary}"):
                rawanalysis = analyze_rep(headline, summary)
                if rawanalysis is None:
                    continue
                try:
                    json_analysis = json.loads(rawanalysis)
                except json.JSONDecodeError:
                    print("Failed to decode JSON from analysis")
                    continue
                print("\nNow parsing information through Bayesian intelligence system")
                analysis = process(json_analysis, url)
                posterior = bayesian(analysis)
                print(json.dumps({
                    "headline": analysis["headline"],
                    "impact_summary": analysis["impact_summary"],
                    "bias": analysis["bias"],
                    "confidence": analysis["confidence"],
                    "posterior": posterior,
                }, indent=2))
            else:
                print('Not a relevant macroeconomic event')

        print("Sleeping for 60 seconds...\n")
        time.sleep(60)

main()
