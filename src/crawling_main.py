from bs4 import BeautifulSoup
import requests
import json
import os
import hashlib
import textwrap
import argparse
import logging
from crontab import CronTab

from item.ranking_item import RankingItem

BASE_URL = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = f'{BASE_DIR}/data.json'

UPDATE_NEWS_URL = 'http://localhost:8080/update_news'

if not os.path.exists(f'{BASE_DIR}/../log'):
  os.makedirs(f'{BASE_DIR}/../log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f'{BASE_DIR}/../log/crawling.log', mode='w')
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] (%(filename)s:%(lineno)d) > %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
cron = CronTab(user=True)

def convert_to_ranking_item(rankingItemDiv):
  rankingThumbDiv = rankingItemDiv.find('div', class_='ranking_thumb')
  rankingTextDiv = rankingItemDiv.find('div', class_='ranking_text')

  headlineDiv = rankingTextDiv.find('div', class_='ranking_headline')
  ledeDiv = rankingTextDiv.find('div', class_='ranking_lede')
  officeDiv = rankingTextDiv.find('div', class_='ranking_office')
  viewDiv = rankingTextDiv.find('div', class_='ranking_view')

  item = RankingItem()
  if rankingThumbDiv is not None:
    item.image_link = rankingThumbDiv.a.img.get('src')
  item.link = 'https://news.naver.com' + headlineDiv.a.get('href')
  item.headline = headlineDiv.a.get('title')
  item.lede = ledeDiv.text.strip()
  item.office = officeDiv.text
  item.view = int(viewDiv.text.replace(',', ''))
  return item

def get_crawling_data(sectionId=105, num=30, date=None):
  url = f'{BASE_URL}&sectionId={sectionId}'
  if date:
    url = f'{url}&date={date}'

  # get html
  response = requests.get(url)
  logger.info("requests.get(url), url: " + url)
  html = response.text

  # parse html & get python object
  soup = BeautifulSoup(html, 'html.parser')
  rankingItems = soup.find_all('li', class_='ranking_item')

  # convert to RankingItem
  rankingItemList = []
  for idx in range(0, num):
    item = convert_to_ranking_item(rankingItems[idx])
    item.rank = idx + 1
    rankingItemList.append(item)
  return rankingItemList

def process_crawling_data(ranking_list):
  # get before ranking from data.json
  before_ranking_dict = read_json_datafile()

  # set previous item and set new ranking
  ranking_dict = {}
  for item in ranking_list:
    hash_id_obj = hashlib.sha256()
    hash_id_obj.update(item.headline.encode('UTF-8'))
    id = hash_id_obj.hexdigest()
    # id = hash(item.link)
    item.id = id
    if before_ranking_dict.get(id) is None:
      item.previous_item = None
    else:
      item.previous_item = RankingItem.from_dict(
        before_ranking_dict.get(id))
      item.previous_item.previous_item = None
      pass
    ranking_dict[id] = item.to_dict()
  
  # write new ranking to data.json
  write_json_datafile(ranking_dict)

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

def notify_to_server():
  response = requests.get(UPDATE_NEWS_URL)
  logger.info("requests.get(UPDATE_NEWS_URL), UPDATE_NEWS_URL: " + UPDATE_NEWS_URL)

def cron_job_start():
  if cron_job_ls() is True:
    print("Already running crawling daemon")
  else:
    job = cron.new(command=f'{BASE_DIR}/../venv/bin/python {BASE_DIR}/crawling_main.py', comment="crawling-daemon")
    job.minute.every(1)
    cron.write()
    print("Start crawling daemon")
    
def cron_job_stop():
  cron.remove_all()
  cron.write()
  print("Stop crawling daemon")

def cron_job_ls():
  if len(cron) == 0:
    return False
  else:
    return True

def main():
  # get ranking data
  ranking_list = get_crawling_data()

  # process data
  process_crawling_data(ranking_list)

  logger.info("RUN Crawling, update crawling data(data.json)")

  # notify to server 
  notify_to_server()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(usage='%(prog)s -c [command]')
  parser.add_argument('-c', metavar='-c', type=str, nargs='?',
                      help='command for processing crontab', choices=['start', 'stop', 'status'])
  args = parser.parse_args()

  if args.c is None:
    main()
  elif args.c == 'start':
    cron_job_start()
  elif args.c == 'stop':
    cron_job_stop()
  else:
    print(cron_job_ls())
