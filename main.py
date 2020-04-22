#!/usr/bin/env python
#-*-coding: utf-8-*-

import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard',methods=["POST"])
def Keyboard():

    contents = {
        "type"     : "keyboard",
        "buttons" : [ "Hi" ]
    }

    return jsonify( contents )

@app.route('/mouce',methods=["GET"])
def Mouce():

    contents = {
        "type"     : "mouce",
        "buttons" : [ "Hi" ]
    }

    return jsonify( contents )

if __name__ == "__main__":
    app.run( host = '0.0.0.0', port = 7000 )