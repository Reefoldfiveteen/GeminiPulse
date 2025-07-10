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
You're a crypto content creator. Write **exactly one** tweet (max 280 characters) about the topic: "{selected_topic}".

- Do NOT give multiple options.
- Do NOT include headings, explanation, or markdown like "**Option 1**".
- Just return a single, fun, clean tweet ready to be posted on X (Twitter).
- End with 2–4 relevant hashtags.
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
