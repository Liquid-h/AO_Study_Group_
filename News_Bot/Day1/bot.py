import requests
import feedparser
import os

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")
RSS_URL = "https://news.hada.io/rss/news"

for i in range(5):
    entry = feed.entries[i]
    title = entry.title
    link = entry.link
    news_text += f"{i+1}. [{title}]({link})\n"

message = {"content": news_text}
response = requests.post(WEBHOOK_URL, json=message)
