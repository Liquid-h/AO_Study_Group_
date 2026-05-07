import requests
import feedparser
import os
import re

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")
RSS_URL = "https://news.hada.io/rss/news"

# HTML 태그를 제거하는 함수
def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext.strip()

feed = feedparser.parse(RSS_URL)

news_text = "📰 **오늘의 긱뉴스(GeekNews) 탑 5**\n\n"

limit = min(5, len(feed.entries))
for i in range(limit):
    entry = feed.entries[i]
    title = entry.title
    link = entry.link
    
    # RSS에서 요약/본문 가져오기 (HTML 태그 제거)
    summary = getattr(entry, 'summary', '')
    summary = clean_html(summary)
    
    # 너무 길면 1~2줄 분량(약 120자)으로 자르기
    if len(summary) > 120:
        summary = summary[:120] + "..."
        
    # 디스코드 인용구(>) 마크다운을 사용해 본문 아래에 요약 추가
    news_text += f"{i+1}. [{title}](<{link}>)\n> {summary}\n\n"

message = {"content": news_text}
response = requests.post(WEBHOOK_URL, json=message)

if response.status_code == 204:
    print("메시지 전송 성공!")
else:
    print(f"메시지 전송 실패: {response.status_code, response.text}")
