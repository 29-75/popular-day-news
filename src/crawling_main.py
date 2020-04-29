from bs4 import BeautifulSoup
import requests
import json
import os

from item.ranking_item import RankingItem

BASE_URL = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day'
DATA_FILE = 'data.json'


def convert_to_ranking_item(rankingItemDiv):
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

def get_popular_day_ranking(sectionId=105, num=30, date = None):
  url = f'{BASE_URL}&sectionId={sectionId}'
  if date:
    url = f'{url}&date={date}'

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
    item = convert_to_ranking_item(rankingItems[idx])
    item.rank = idx + 1
    rankingItemList.append(item)
  return rankingItemList

def read_json_datafile():
  if os.path.isfile(DATA_FILE):
    with open(DATA_FILE, 'r') as data_file:
      before_raw_json = data_file.read().encode('utf-8')
      before_ranking_json = json.loads(before_raw_json)
    return before_ranking_json
  else:
    return {}


def write_json_datafile(ranking_dict):
  with open(DATA_FILE, 'w') as data_file:
    json.dump(ranking_dict, data_file, ensure_ascii=False)


def main():
  # get ranking
  ranking_list = get_popular_day_ranking()
    
  # get before ranking from data.json
  before_ranking_dict = read_json_datafile()

  # set previous item and set new ranking
  ranking_dict = {}
  for item in ranking_list:
    # id = hash(item.link)
    id = hash(item.link)
    item.id = id
    if before_ranking_dict.get(id) is None:
      item.previous_item = None
    else:
      item.previous_item = RankingItem.from_dict(before_ranking_dict.get(id))
      item.previous_item.previous_item = None
      pass
    ranking_dict[id] = item.to_dict()
  
  # write new ranking to data.json
  write_json_datafile(ranking_dict)

if __name__ == "__main__":
  main()
