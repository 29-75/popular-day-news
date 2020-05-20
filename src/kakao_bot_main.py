from urllib import request
from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route('/update_news', methods=["GET"])
def update_news():
    url = 'http://pf.kakao.com/_AiDaxb'
    #url = 'http://pf.kakao.com/_AiDaxb/chat'
    headers = {'Authorization': 'Bearer [YOUR_ACCESS_TOKEN]'}

    # read data.Json file
    with open('data.json', encoding='UTF8') as json_file:
        json_data = json.load(json_file)

    # noti to kakao chat-bot
    # kakaoResponse = requests.post(url, headers=headers, data=json_data)

    #return empty queryString
    re_msg={"version":"2.0","template":{"outputs":[{"simpleText":{"text":json_data}}]}}
    return jsonify(re_msg)

@app.route('/list_all', methods=["POST"])
def ListAll():
    items = []
    if request.method == 'POST':
        # read data.Json file
        with open('data.json', encoding='UTF8') as json_file:
            json_data = json.load(json_file)
            for context in json_data:

                headline = json_data[context]['headline']
                view = json_data[context]['view']
                link = json_data[context]['image_link']

                item = {
                            "type":"",
                            "title": str(headline),
                            "description": str(view),
                            "imageUrl": str(link),
                            "link": {
                                "type": "",
                                "webUrl": str(link),
                                "moUrl": str(link),
                                "pcUrl": str(link),
                                "pcCustomScheme": "",
                                "macCustomScheme": "",
                                "iosUrl": "",
                                "iosStoreUrl": "",
                                "androidUrl": "",
                                "androidStoreUrl": ""
                            }
                        }

                items.append(item)
        response_message={
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "listCard": {
                                "header": {
                                    "title": "🏆 News LIST All",
                                    "imageUrl": "http://k.kakaocdn.net/dn/xsBdT/btqqIzbK4Hc/F39JI8XNVDMP9jPvoVdxl1/2x1.jpg"
                                },
                                "items": items,
                                "buttons": [
                                    {
                                        "label": "구경 가기",
                                        "action": "webLink",
                                        "webLinkUrl": "https://www.naver.com"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        return jsonify(response_message)

@app.route('/top3', methods=["POST"])
def top3():
    items = []
    if request.method == 'POST':
        # read data.Json file
        with open('data.json', encoding='UTF8') as json_file:
            json_data = json.load(json_file)
            for context in json_data:
                if json_data[context]['rank'] <= 3:
                    headline = json_data[context]['headline']
                    view = json_data[context]['view']
                    link = json_data[context]['image_link']

                    item = {
                        "type":"",
                        "title": str(headline),
                        "description": str(view),
                        "imageUrl": str(link),
                        "link": {
                            "type": "",
                            "webUrl": str(link),
                            "moUrl": str(link),
                            "pcUrl": str(link),
                            "pcCustomScheme": "",
                            "macCustomScheme": "",
                            "iosUrl": "",
                            "iosStoreUrl": "",
                            "androidUrl": "",
                            "androidStoreUrl": ""
                        }
                    }
                    items.append(item)
            response_message={
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "listCard": {
                                "header": {
                                    "title": "🏆 News LIST All",
                                    "imageUrl": "http://k.kakaocdn.net/dn/xsBdT/btqqIzbK4Hc/F39JI8XNVDMP9jPvoVdxl1/2x1.jpg"
                                },
                                "items": items,
                                "buttons": [
                                    {
                                        "label": "뉴스보러가기",
                                        "action": "webLink",
                                        "webLinkUrl": "https://news.naver.com/"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        return jsonify(response_message)

@app.route('/top5', methods=["POST"])
def top5():
    items = []
    if request.method == 'POST':
        msg=[]
        # read data.Json file
        with open('data.json', encoding='UTF8') as json_file:
            json_data = json.load(json_file)
            for context in json_data:
                if json_data[context]['rank'] <= 5:
                    headline = json_data[context]['headline']
                    view = json_data[context]['view']
                    link = json_data[context]['image_link']

                    item = {
                        "type":"",
                        "title": str(headline),
                        "description": str(view),
                        "imageUrl": str(link),
                        "link": {
                            "type": "",
                            "webUrl": str(link),
                            "moUrl": str(link),
                            "pcUrl": str(link),
                            "pcCustomScheme": "",
                            "macCustomScheme": "",
                            "iosUrl": "",
                            "iosStoreUrl": "",
                            "androidUrl": "",
                            "androidStoreUrl": ""
                        }
                    }
                    items.append(item)
            response_message={
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "listCard": {
                                "header": {
                                    "title": "🏆 News LIST All",
                                    "imageUrl": "http://k.kakaocdn.net/dn/xsBdT/btqqIzbK4Hc/F39JI8XNVDMP9jPvoVdxl1/2x1.jpg"
                                },
                                "items": items,
                                "buttons": [
                                    {
                                        "label": "뉴스보러가기",
                                        "action": "webLink",
                                        "webLinkUrl": "https://news.naver.com/"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        return jsonify(response_message)

@app.route('/top10', methods=["POST"])
def top10():
    items = []
    if request.method == 'POST':
        msg=[]
        # read data.Json file
        with open('data.json', encoding='UTF8') as json_file:
            json_data = json.load(json_file)
            for context in json_data:
                if json_data[context]['rank'] <= 10:
                    headline = json_data[context]['headline']
                    view = json_data[context]['view']
                    link = json_data[context]['image_link']

                    item = {
                        "type":"",
                        "title": str(headline),
                        "description": str(view),
                        "imageUrl": str(link),
                        "link": {
                            "type": "",
                            "webUrl": str(link),
                            "moUrl": str(link),
                            "pcUrl": str(link),
                            "pcCustomScheme": "",
                            "macCustomScheme": "",
                            "iosUrl": "",
                            "iosStoreUrl": "",
                            "androidUrl": "",
                            "androidStoreUrl": ""
                        }
                    }
                    items.append(item)
            response_message={
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "listCard": {
                                "header": {
                                    "title": "🏆 News LIST All",
                                    "imageUrl": "http://k.kakaocdn.net/dn/xsBdT/btqqIzbK4Hc/F39JI8XNVDMP9jPvoVdxl1/2x1.jpg"
                                },
                                "items": items,
                                "buttons": [
                                    {
                                        "label": "뉴스보러가기",
                                        "action": "webLink",
                                        "webLinkUrl": "https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=105&date=20200520"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        return jsonify(response_message)

@app.route('/keyboard', methods=["POST"])
def Keyboard():
    contents = {
        "type": "keyboard",
        "buttons": ["Hi"]
    }

    return jsonify(contents)


@app.route('/route_name')
def method_name():
    return "hello world"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    pass

