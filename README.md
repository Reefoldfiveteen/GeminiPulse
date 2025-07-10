# GeminiPulse 🔁📈

**GeminiPulse** is an AI-powered crypto bot that monitors real-time market data and automatically posts tweets with smart analysis using Google Gemini AI.

Stay updated on Bitcoin, Ethereum, and other top cryptocurrencies with dynamic insights posted to your X (Twitter) account.

---

## 🌟 Features

- 📡 Fetches live prices from [CoinGecko](https://coingecko.com)
- 📈 Detects market trends (bullish/bearish)
- 🧠 Generates insightful, natural-language tweets using Gemini AI
- 🐦 Posts automatically to Twitter/X
- 🕒 Scheduleable with cron for regular updates

---

## 🚀 Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/GeminiPulse.git
   ```
   ```
   cd GeminiPulse
   ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Configure your credentials**
   Edit file named config.py:
    ```bash
    # Twitter API
    API_KEY = "your_twitter_api_key"
    API_SECRET = "your_twitter_api_secret"
    ACCESS_TOKEN = "your_access_token"
    ACCESS_TOKEN_SECRET = "your_access_token_secret"
    
    # Gemini AI
    GEMINI_API_KEY = "your_gemini_api_key"
    GEMINI_MODEL = "gemini-pro"

    ```
4. **Run the bot**
    ```bash
    python3 bot.py
    ```
    
