import requests
import feedparser
import os

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")
RSS_URL = "https://news.hada.io/rss/news"

feed = feedparser.parse(RSS_URL)

news_text = "📰 **오늘의 긱뉴스(GeekNews) 탑 5**\n\n"

limit = min(5, len(feed.entries))
for i in range(limit):
    entry = feed.entries[i]
    title = entry.title
    link = entry.link
    news_text += f"{i+1}. [{title}](<{link}>)\n"

message = {"content": news_text}
response = requests.post(WEBHOOK_URL, json=message)

if response.status_code == 204:
    print("메시지 전송 성공!")
else:
    print(f"메시지 전송 실패: {response.status_code, response.text}")
