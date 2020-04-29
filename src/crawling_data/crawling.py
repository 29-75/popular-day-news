import requests
from bs4 import BeautifulSoup
import json

BASE_URL = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day'


class RankingItem:
  id = 0
  rank = 0
  image_link = None
  link = None
  headline = None
  lede = None
  office = None
  view = 0
  previous_item = None

  def to_dict(self):
    return {
      'id': self.id,
      'rank': self.rank,
      'image_link': self.image_link,
      'link': self.link,
      'headline': self.headline,
      'lede': self.lede,
      'office': self.office,
      'view': self.view,
      'previous_item': {} if self.previous_item is None else self.previous_item.to_dict()
    }
  
  @staticmethod
  def from_dict(dictObj):
    item = RankingItem()
    item.id = dictObj['id']
    item.rank = dictObj['rank']
    item.image_link = dictObj['image_link']
    item.link = dictObj['link']
    item.headline = dictObj['headline']
    item.lede = dictObj['lede']
    item.office = dictObj['office']
    item.view = dictObj['view']
    item.previous_item = None if dictObj['previous_item'] == {} else RankingItem.from_dict(dictObj['previous_item'])
    return item

  def print_item(self):
    print('======================== print_item ========================')
    print(f'    id: {self.id}')
    print(f'    rank: {self.rank}')
    print(f'    image_link: {self.image_link}')
    print(f'    link: {self.link}')
    print(f'    headline: {self.headline}')
    print(f'    lede: {self.lede}')
    print(f'    office: {self.office}')
    print(f'    view: {self.view}')

def convertToRankingItem(rankingItemDiv):
  rankingThumbDiv = rankingItemDiv.find('div', class_='ranking_thumb')
  rankingTextDiv = rankingItemDiv.find('div', class_='ranking_text')

  headlineDiv = rankingTextDiv.find('div', class_='ranking_headline')
  ledeDiv = rankingTextDiv.find('div', class_='ranking_lede')
  officeDiv = rankingTextDiv.find('div', class_='ranking_office')
  viewDiv = rankingTextDiv.find('div', class_='ranking_view')

  item = RankingItem()
  item.image_link = rankingThumbDiv.a.img.get('src')
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
    item.rank = idx + 1
    rankingItemList.append(item)

  return rankingItemList

if __name__ == "__main__":
  sectionId = '105'
  date = '20200416'
  url = BASE_URL + '&sectionId=' + sectionId + '&date=' + date

  # get ranking
  ranking_list = getPopularDayRanking(sectionId, date, 30)
    
  # get before ranking from data.json
  read_file = open('../data.json', 'r')
  before_ranking_json = read_file.read()
  before_ranking_dict = json.loads(before_ranking_json)
  read_file.close()  

  # set previous item and set new ranking
  ranking_dict = {}
  for item in ranking_list:
    # id = hash(item.link)
    id = item.link
    item.id = id
    if before_ranking_dict.get(id) is None:
      item.previous_item = None
    else:
      item.previous_item = RankingItem.from_dict(before_ranking_dict.get(id))
      item.previous_item.previous_item = None
      pass
    ranking_dict[id] = item.to_dict()
  
  # write new ranking to data.json
  write_file = open('../data.json', 'w')
  ranking_json = json.dumps(ranking_dict)
  write_file.write(ranking_json)
  write_file.close()


  

  

  

