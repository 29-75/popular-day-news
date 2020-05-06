from flask import Flask, request, jsonify, redirect
from item.ranking_item import RankingItem
import sys, json, os
app = Flask(__name__)

buttons_list = ['List All', 'Top 3', 'Top 5', '카테고리검색']

# 5.1 Home Keyboard API
@app.route('/keyboard')
def Keyboard():
    return jsonify({
        'type': 'buttons',
        'buttons': buttons_list 
    })

# 5.2 메세지 수진 및 자동응답 API
@app.route('/message', methods=['POST'])
def Message():
    content = request.get_json()
    user_key = content['user_key']
    user_type = content['type']
    print("user key : ", user_key)
    msg = []
    if user_type == "buttons":
        user_input = content['content']
        if user_input == buttons_list[0]: # List All
            with open('data.json') as json_file:
                json_data = json.load(json_file)
            response_data = json_data
        elif user_input == buttons_list[1]: # List Top 3
            with open('data.json') as json_file:
                json_data = json.load(json_file)
                for i in json_data:
                    if json_data[i]['rank'] <=3:
                        msg.append(json_data[i])
            response_data = msg
        elif user_input == buttons_list[2]: # List Top 5
            with open('data.json') as json_file:
                json_data = json.load(json_file)
                for i in json_data:
                    if json_data[i]['rank'] <=5:
                        msg.append(json_data[i])
            response_data = msg
        elif user_input == buttons_list[3]: # 카테고리 검색
            response_data = {
                'message' : {
                    "text": '카테고리를 입력해주세요.'
                },
                'keyboard' : {
                    'type' : "text"
                }
            }
        else :
            response_data = {
                'message' : {
                    "text": '지원하지 않는 메뉴입니다.'
                }
            }
        return jsonify(response_data)
    elif user_type == "text":
        user_input = content['content']
        if user_input.lower() == u"cloud":
            with open('data.json') as json_file:
                json_data = json.load(json_file)
                for i in json_data:
                    if json_data[i]['headline'].lower() == u"cloud":
                        msg.append(json_data[i])
            response_data.append(msg)             
        elif user_input.lower() == u"tmax":
            with open('data.json') as json_file:
                json_data = json.load(json_file)
                for i in json_data:
                    if json_data[i]['headline'].lower() == u"tmax":
                        msg.append(json_data[i])
            response_data.append(msg)            
        else :
            response_data = {
                'message' : {
                    "text": '지원하지 않는 메뉴입니다.'
                }
            }
        return jsonify(response_data)

# 5.3 친구 추가 / 차단 API
@app.route('/friend', methods=['POST', 'DELETE'])
def friend():
    if request.method == 'POST':
        content = request.get_json()
        user_key = content['user_key']
        print(user_key)        
        return '', 200
    elif request.method == 'DELETE':
        return '', 200
    else : 
        return "Invalid method"

# 5.4 채팅방 나가기
@app.route('/chat_room/:user_key', methods=['DELETE'])
def chat_out():
# /chat_room/HASHED_USER_KEY -> 이 값으로 user 관리 서버에 전달
    return '', 200

# test code
@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        return "POST method called"
    elif request.method == 'GET':
        with open('data.json') as json_file:
            json_data = json.load(json_file)
        #people = [{'name': 'Alice', 'birth-year': 1986},
        #                  {'name': 'Bob', 'birth-year': 1985}]
        myitem = RankingItem.from_dict(json_data)
        print("my item : ",myitem)
        for i in json_data:
            #print(json_data[i]
            print("id : " , json_data[i]['id'])
            
        return jsonify(json_data) 
    else :
        return "Invalid method"


# check server
@app.route('/')
def Hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

# error handler
#@app.errorhandler


# TODO : API Specifications
# 1. 응답 지연시간 5초 안에 응답 없을 경우 응답없음 메세지 발송
# 2. QOS : 응답 실패 10회 이상부터는 해당 모듈 장애 메세지로 변경. 앱 관리자에게 메일 발송
# 3. 개발자 서버 URL 호출
# 4. 