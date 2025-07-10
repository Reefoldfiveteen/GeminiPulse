import tweepy
import config
import google.generativeai as genai
from datetime import datetime, timezone
import random

# Inisialisasi Gemini
genai.configure(api_key=config.GEMINI_API_KEY)
model = genai.GenerativeModel(config.GEMINI_MODEL)

# Daftar topik random berbahasa Indonesia
TOPIK = [
    "tips bertahan saat pasar crypto turun",
    "candaan receh tentang Bitcoin",
    "sindiran lucu untuk altcoin rugpull",
    "motivasi buat yang nyangkut di crypto",
    "kesalahan pemula saat trading",
    "cara tetap waras di bear market",
    "quotes singkat tentang HODL",
    "sindiran buat yang FOMO",
    "kenangan saat bull run",
    "crypto dari sudut pandang emak-emak"
]

def generate_random_tweet_indo():
    topik = random.choice(TOPIK)
    prompt = f"""
Tulis satu tweet singkat dalam Bahasa Indonesia (maks 280 karakter) tentang topik: "{topik}".

- Gunakan gaya santai dan lucu kalau bisa.
- Jangan beri beberapa opsi. Cukup satu tweet saja.
- Hindari penjelasan atau heading.
- Tambahkan 2–4 hashtag yang relevan di akhir.
"""
    response = model.generate_content(prompt)
    return response.text.strip()

def post_tweet():
    tweet = generate_random_tweet_indo()
    if len(tweet) > 280:
        print("❌ Tweet terlalu panjang, skip.")
        return

    print("📝 Tweet Indo:", tweet)

    client = tweepy.Client(
        consumer_key=config.API_KEY,
        consumer_secret=config.API_SECRET,
        access_token=config.ACCESS_TOKEN,
        access_token_secret=config.ACCESS_TOKEN_SECRET
    )

    try:
        response = client.create_tweet(text=tweet)
        print("✅ Tweet posted:", response)
    except Exception as e:
        print("❌ Gagal post tweet:", e)

if __name__ == "__main__":
    post_tweet()
