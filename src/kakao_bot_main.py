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
                            'title': str(headline),
                            'description': str(view),
                            'imageUrl': str(link),
                            'link': {
                                'web': str(link)
                            }
                        }

                items.append(item)
        response_message={
                'version': "2.0",
                'template': {
                    'outputs': [
                        {
                            'listCard': {
                                'header': {
                                    'title': '🏆 News LIST All'
                                },
                                'items': items,
                            }
                        }
                    ]
                }
            }
        return jsonify(response_message)

@app.route('/top3', methods=["POST"])
def top3():
    if request.method == 'POST':
        msg=[]
        # read data.Json file
        with open('data.json', encoding='UTF8') as json_file:
            json_data = json.load(json_file)
            for context in json_data:
                if json_data[context]['rank'] <= 3:
                    print(json_data[context]['headline'])
                    print(json_data[context]['rank'])
                    re_msg={"version":"2.0",
                            "template":
                                {"outputs":
                                     {"text": "top 3 기사 결과 입니다.",
                                      "HeadLine" : json_data[context]['headline'],
                                      "Rank" : json_data[context]['rank'],
                                      "keyboard": {"type": "text"}
                                      }
                                 }
                            }

                    msg.append(re_msg)

        return jsonify(msg)


@app.route('/top5', methods=["POST"])
def top5():
    if request.method == 'POST':
        msg=[]
        # read data.Json file
        with open('data.json', encoding='UTF8') as json_file:
            json_data = json.load(json_file)
            for context in json_data:
                if json_data[context]['rank'] <= 5:
                    print(json_data[context]['headline'])
                    print(json_data[context]['rank'])
                    re_msg={"version":"2.0",
                            "template":
                                {"outputs":
                                     {"text": "top 3 기사 결과 입니다.",
                                      "HeadLine" : json_data[context]['headline'],
                                      "Rank" : json_data[context]['rank'],
                                      "keyboard": {"type": "text"}
                                      }
                                 }
                            }
                    msg.append(re_msg)

        return jsonify(msg)

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

