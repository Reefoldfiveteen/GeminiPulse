import tweepy
import config
import google.generativeai as genai
from datetime import datetime, timezone
import random

# Inisialisasi Gemini
genai.configure(api_key=config.GEMINI_API_KEY)
model = genai.GenerativeModel(config.GEMINI_MODEL)

# Daftar topik acak
TOPICS = [
    "crypto meme idea",
    "funny crypto quote",
    "crypto beginner tips",
    "weird crypto terminology explained",
    "crypto mindset advice",
    "crypto FOMO warning",
    "short joke about altcoins",
    "1-sentence crypto motivation",
    "bear market survival tip",
    "bull run tweet for engagement"
]

def generate_random_topic_tweet():
    selected_topic = random.choice(TOPICS)
    prompt = f"""
Generate a tweet (max 280 characters) on the following topic: "{selected_topic}".
Make it witty, concise, and engaging for crypto X users. Avoid boring or generic stuff.
"""
    response = model.generate_content(prompt)
    return response.text.strip()

def post_tweet():
    tweet = generate_random_topic_tweet()
    print("📝 Random Tweet:", tweet)

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
        print("❌ Failed to post tweet:", e)

if __name__ == "__main__":
    post_tweet()
