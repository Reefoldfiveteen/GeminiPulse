import tweepy
import requests
import config
from datetime import datetime
import google.generativeai as genai

def get_crypto_price(ids=["bitcoin", "ethereum"], currency="usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(ids),
        "vs_currencies": currency,
        "include_24hr_change": "true"
    }
    res = requests.get(url, params=params)
    return res.json()

def format_for_prompt(data):
    lines = []
    for coin, info in data.items():
        name = coin.capitalize()
        price = info['usd']
        change = info['usd_24h_change']
        trend = "up" if change > 0 else "down"
        lines.append(f"{name}: ${price:,.2f} ({change:+.2f}%) - {trend}")
    return "\n".join(lines)

def generate_tweet(prompt):
    genai.configure(api_key=config.GEMINI_API_KEY)
    model = genai.GenerativeModel(config.GEMINI_MODEL)
    response = model.generate_content(prompt)
    return response.text.strip()

def post_tweet():
    data = get_crypto_price()
    now = datetime.now().strftime("%d %b %Y, %H:%M WIB")

    market_summary = format_for_prompt(data)
    prompt = f"""
You are a crypto analyst bot. Generate 1 short tweet (under 280 characters) that summarizes the current crypto market condition with prices and trend.
Be casual, informative, and use varied natural language. Include the current time: {now}.
Here is the data:

{market_summary}
    """

    tweet = generate_tweet(prompt)
    print("Generated Tweet:", tweet)

    # ==== v2 Client for Posting Tweet ====
    client = tweepy.Client(
        consumer_key=config.API_KEY,
        consumer_secret=config.API_SECRET,
        access_token=config.ACCESS_TOKEN,
        access_token_secret=config.ACCESS_TOKEN_SECRET
    )

    response = client.create_tweet(text=tweet)
    print("✅ Tweet posted:", response)

if __name__ == "__main__":
    post_tweet()
