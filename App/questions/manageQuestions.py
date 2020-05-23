import sqlite3
import os
import json

#conn = sqlite3.connect('questions.db')

#c = conn.cursor()

# c.execute('''CREATE TABLE `ques_and_answers` (
# 	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
# 	`question`	TEXT NOT NULL,
# 	`answer`	TEXT NOT NULL,
# )''')
#
# conn.commit()
# conn.close()
class chat_manage:
	c = None
	def __init__(self):
		current_path = os.path.dirname(os.path.realpath(__file__))

		self.c = sqlite3.connect(current_path + '/questions.db', check_same_thread=False).cursor()
	def getAllQuestion(self):
		query = 'SELECT * FROM ques_and_answers'		
		self.c.execute(query)
		result = self.c.fetchall()
		return result
	def getQuestion(self, question):
		query = 'SELECT * FROM ques_and_answers WHERE question="' + str(question) + '"'
		# print(query)
		self.c.execute(query)
		result = self.c.fetchone()
		return result