FROM python

EXPOSE 8080

COPY ./src .
COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install -y cron

RUN pip install -r requirements.txt

CMD service cron start ; python crawling_main.py -c start ; python kakao_bot_main.py
