import requests
import feedparser
import os

# 깃허브 서버에 숨겨둔 비밀번호(웹훅 주소)를 불러옵니다.
WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")
RSS_URL = "https://news.hada.io/rss/news"

print("📡 긱뉴스 최신 글을 가져오는 중...")
feed = feedparser.parse(RSS_URL)

news_text = "🔥 **오늘 아침 최신 테크 뉴스** 🔥\n\n"

for i in range(5):
    entry = feed.entries[i]
    title = entry.title
    link = entry.link
    news_text += f"{i+1}. [{title}]({link})\n"

message = {"content": news_text}
response = requests.post(WEBHOOK_URL, json=message)

if response.status_code == 204:
    print("🎉 전송 완료!")
else:
    print(f"❌ 전송 실패: {response.status_code}")