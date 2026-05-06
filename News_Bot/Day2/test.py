import feedparser
import os

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")
RSS_URL = "https://news.hada.io/rss/news" # 가져올 기사의 링크 등

for i in range(5):
    entry = feed.entries[i]
    title = entry.title
    link = entry.link
    news_text += f"{i+1}. [{title}]({link})\n"

message = {"content": news_text}
response = requests.post(WEBHOOK_URL, json=message)

# 이 코드를 통해 다양한 기사를 크롤링하고 개시함
