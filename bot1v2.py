import tweepy
import requests
import config
from datetime import datetime, timezone
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
    now = datetime.now(timezone.utc).strftime("%d %b %Y, %H:%M UTC")

    market_summary = format_for_prompt(data)

    # ✍️ Prompt utama
    prompt_main = f"""
You're a crypto analyst. Write 1 short tweet (under 280 chars) summarizing trending crypto prices and movement.
Make it fun and engaging. Time: {now}.
Here’s the data:\n{market_summary}
    """

    tweet_main = generate_tweet(prompt_main)
    print("Main Tweet:", tweet_main)

    # ✍️ Prompt lanjutan thread
    prompt_thread = f"""
Now write a follow-up tweet (under 280 chars) giving quick thoughts on market sentiment or advice to holders based on the same data.
Mention emotions, momentum, or common behavior (FOMO, HODL, etc).
    """

    tweet_thread = generate_tweet(prompt_thread)
    print("Thread Tweet:", tweet_thread)

    # 🔁 Post via Twitter v2
    client = tweepy.Client(
        consumer_key=config.API_KEY,
        consumer_secret=config.API_SECRET,
        access_token=config.ACCESS_TOKEN,
        access_token_secret=config.ACCESS_TOKEN_SECRET
    )

    # Post tweet utama
    response_main = client.create_tweet(text=tweet_main)
    tweet_id = response_main.data["id"]

    # Post tweet lanjutan sebagai balasan
    response_thread = client.create_tweet(text=tweet_thread, in_reply_to_tweet_id=tweet_id)

    print("✅ Main + Thread Tweet posted.")


if __name__ == "__main__":
    post_tweet()
