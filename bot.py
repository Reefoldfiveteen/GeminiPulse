import tweepy
import requests
import config
from datetime import datetime
import google.generativeai as genai

# --- Twitter Auth
def auth_twitter():
    auth = tweepy.OAuth1UserHandler(
        config.API_KEY, config.API_SECRET,
        config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET
    )
    return tweepy.API(auth)

# --- Ambil harga crypto
def get_crypto_price(ids=["bitcoin", "ethereum"], currency="usd"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(ids),
        "vs_currencies": currency,
        "include_24hr_change": "true"
    }
    res = requests.get(url, params=params)
    return res.json()

# --- Format data untuk prompt
def format_for_prompt(data):
    lines = []
    for coin, info in data.items():
        name = coin.capitalize()
        price = info['usd']
        change = info['usd_24h_change']
        trend = "naik" if change > 0 else "turun"
        lines.append(f"{name}: ${price:,.2f} ({change:+.2f}%) - {trend}")
    return "\n".join(lines)

# --- Generate kalimat dengan Gemini
def generate_tweet(prompt):
    genai.configure(api_key=config.GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text.strip()

# --- Posting ke Twitter
def post_tweet():
    api = auth_twitter()
    data = get_crypto_price()
    now = datetime.now().strftime("%d %b %Y, %H:%M")

    market_summary = format_for_prompt(data)
    prompt = f"""
Kamu adalah analis crypto. Buatkan 1 tweet singkat (maks 280 karakter) yang menyimpulkan harga crypto saat ini dan tren naik/turunnya. 
Gunakan gaya bahasa yang santai, menarik, dan bervariasi. Sertakan waktu sekarang: {now}.
Berikut ini datanya:

{market_summary}
    """

    tweet = generate_tweet(prompt)
    print("Generated Tweet:", tweet)
    
    api.update_status(tweet)
    print("✅ Tweet terkirim.")

if __name__ == "__main__":
    post_tweet()
