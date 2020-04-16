from flask import Flask


app = Flask(__name__)

@app.route('/route_name')
def method_name():
	 return "hello world"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
    pass
