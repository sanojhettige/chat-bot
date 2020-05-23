# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import sqlite3
import json

from questions import manageQuestions
from questions import questionAdapter

# Constants
DB_PATH = "questions/questions.db";

# Message types
GREETING_LABEL = 'greeting'
ACCOUNT_TYPE='account_type'
UNKNOWN = 'unknown'
USERNAME=''

# Facebook connect to messenger
PAGE_ACCESS_TOKEN = ''
VERIFY_TOKEN = ''
FB_API_URL = ''

app = Flask(__name__)
CORS(app)
api = Api(app)

# DB Connection
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

QuestionAdapter = questionAdapter.QuestionAdapter()

# Set Response for the user activity
def getBotResponse(query):
	result = QuestionAdapter.find_answer(query)
	return result

# Get reponse from server
@app.route("/getresponse", methods=['POST'])
def getresponse():
	text_messenger = request.form['query']
	return getBotResponse(text_messenger)

if __name__ == '__main__':
	x = getBotResponse("hi")
	print(json.loads(x).get('status'))
	run = app.run(port=4000, debug=False)