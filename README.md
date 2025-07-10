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
   git clone https://github.com/Reefoldfiveteen/GeminiPulse.git
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

    **🔐 Gemini API?**
   
   Open: [Gemini API]([https://coingecko.com](https://makersuite.google.com/app/apikey))
   
5. **Run the bot**
    ```bash
    python3 bot.py
    ```

---
## ⏰ Automate with Cron (Optional)
To schedule auto-posting every hour:
```
crontab -e
```
Add this line:
```
0 * * * * cd /path/to/GeminiPulse && /usr/bin/python3 bot.py >> log.txt 2>&1
```
---
## 📤 Example Tweet Output
🔥 Market Pulse (Jul 10, 2025, 10:00 AM)
Bitcoin surged to $66,800 📈
Ethereum follows with +3.1%!
Is this the start of a bull wave? 🐂🚀

---
## 🛠 Tech Stack
* CoinGecko API – Real-time market data
* Google Gemini AI – Language generation
* Tweepy – Twitter/X API integration
* Python 3 – Core runtime

---
## 🧠 Use Case Ideas
* Run as a personal market analyst bot
* Integrate with Discord for multi-platform alerts
* Expand to include charts, RSI/MA trends, or on-chain data

---
## ⚠️ Disclaimer
This project is for educational and informational purposes only. It does not provide financial advice. Trade responsibly.

---
## 📄 License
MIT License – Free to use, modify, and share with proper attribution.


