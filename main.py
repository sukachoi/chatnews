#챗gpt 뉴스 봇 만들어서 텔레그렘으로 받아보기
# 뉴스를 크롤링함.
# 크롤링한 결과로 메세지를 만든다.
# 메세지를 텔레그램으로 보낸다.
#bot name chatgptsukabot
#6593939004:AAFTX-_Zqh7GAFsnkMphspP2KuftcMjzvW8
##@sdfdsfsdf
import requests
from bs4 import BeautifulSoup
import telegram
# 서치 키워드
search_word = '챗gpt'

# 기존에 보냈던 링크를 담아둘 리스트
old_links = []

# 스크래핑 함수 
def extract_links(old_links=[]):
    url = f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_jum&query={search_word}'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    search_result = soup.select_one('#news_result_list')
    news_list = search_result.select('.bx > .news_wrap > a')

    links = []
    for news in news_list[:5]:
        link = news['href']
        links.append(link)
    
    new_links=[]
    for link in links:
        if link not in old_links:
            new_links.append(link)
    
    return new_links

# 이전 링크를 매개변수로 받아서, 비교 후 새로운 링크만 출력
# 차후 이 부분을 메시지 전송 코드로 변경하고 매시간 동작하도록 설정
# 새로운 링크가 없다면 빈 리스트 반환

new_links = extract_links(old_links)
print('===보낼 링크===\n', new_links,'\n')

text = str(new_links)


import telegram, datetime as dt, time
import asyncio

chat_token = "6593939004:AAFTX-_Zqh7GAFsnkMphspP2KuftcMjzvW8"

bot = telegram.Bot(chat_token)
url = 'https://api.telegram.org/bot'+chat_token+'/getUpdates'
response = requests.get(url)
id = 6559684700#response.json()['result'][0]['message']['chat']['id']
#정리하면 chat_id를 알아내는 방법이 바뀜.
#https://api.telegram.org/bot6593939004:AAFTX-_Zqh7GAFsnkMphspP2KuftcMjzvW8/getUpdates

#20230813 9시42분 아이디를 하드코딩으로 바꿈

"""
print(response.json()['result'])
print("----------------------------------------------------")
print(response.json()['result'][0])
print("----------------------------------------------------")
print(response.json()['result'][0]['message'])
print("----------------------------------------------------")
print(response.json()['result'][0]['message']['chat'])
print("----------------------------------------------------")
print(response.json()['result'][0]['message']['chat']['id'])
"""
asyncio.run(bot.sendMessage(chat_id = id, text=text))
