import requests
from bs4 import BeautifulSoup

SEED_URL = 'https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=105'


if __name__ == "__main__":
	# HTTP GET Request
	req = requests.get(SEED_URL)
	html = req.text

	# BeautifulSoup으로 html소스를 python객체로 변환하기
	# 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
	# 이 글에서는 Python 내장 html.parser를 이용했다.
	soup = BeautifulSoup(html, 'html.parser')

	#wrap > table > tbody > tr > td.content > div > div.ranking > ol > li.ranking_item.is_num1 > div.ranking_text > div.ranking_headline > a
	#wrap > table > tbody > tr > td.content > div > div.ranking > ol > li.ranking_item
	#wrap > table > tbody > tr > td.content > div > div.ranking > ol > li.ranking_item > div.ranking_text > div.ranking_headline > a
	my_titles = soup.select('div.ranking > ol > li.ranking_item > div.ranking_text > div.ranking_headline > a')
	print(f'crawling length: {len(my_titles)}')

	# print(my_titles[0].text)

	for idx in range(0, len(my_titles)):
		print(f'{idx}. {my_titles[idx].text}')

	# for title in my_titles:
	# 	# Tag안의 텍스트
	# 	print(title.text)
	# 	# Tag의 속성을 가져오기(ex: href속성)
	# 	print(title.get('href'))
