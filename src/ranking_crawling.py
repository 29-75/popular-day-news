import requests
from bs4 import BeautifulSoup
from ranking import RankingItem

BASE_URL = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day'

def convertToRankingItem(rankingItemDiv):
    rankingTextDiv = rankingItemDiv.find('div', class_='ranking_text')

    headlineDiv = rankingTextDiv.find('div', class_='ranking_headline')
    ledeDiv = rankingTextDiv.find('div', class_='ranking_lede')
    officeDiv = rankingTextDiv.find('div', class_='ranking_office')
    viewDiv = rankingTextDiv.find('div', class_='ranking_view')

    item = RankingItem()
    item.link = headlineDiv.a.get('href')
    item.headline = headlineDiv.a.get('title')
    item.lede = ledeDiv.text.strip()
    item.office = officeDiv.text
    item.view = int(viewDiv.text.replace(',', ''))

    return item

def getPopularDayRanking(sectionId, date, num):
    url = BASE_URL + '&sectionId=' + sectionId + '&date=' + date
    # get html 
    response = requests.get(url)
    print("requests.get(url), url: " + url)
    html = response.text

    # parse html & get python object
    soup = BeautifulSoup(html, 'html.parser')
    rankingItems = soup.find_all('li', class_='ranking_item')

    # convert to RankingItem
    rankingItemList  = []
    for idx in range(0, num):
        item = convertToRankingItem(rankingItems[idx])
        item.num = idx + 1
        rankingItemList.append(item)

    return rankingItemList

if __name__ == "__main__":
    sectionId = '105'
    date = '20200416'
    url = BASE_URL + '&sectionId=' + sectionId + '&date=' + date

    rankingItemList = getPopularDayRanking(sectionId, date, 30)
    for idx in range(0, len(rankingItemList)):
        rankingItemList[idx].printItem()






