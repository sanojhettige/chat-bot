#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyvi import ViTokenizer, ViPosTagger
import io
from nltk import ngrams
from string import punctuation
import os
import sqlite3
import json

from . import manageQuestions
current_path = os.path.dirname(os.path.realpath(__file__))
manager = manageQuestions.chat_manage()

class QuestionAdapter(object):

	def __init__(self):
		print("init QuestionAdapter")

	def find_answer(self, query):

		allquestion = manager.getAllQuestion()
		# print(allquestion)
		query = ''.join(c for c in query if c not in punctuation)
		filterd_query = list(ngrams(query.split(), 1)) + list(ngrams(query.split(), 2))
		set_query = set([" ".join(gram).lower() for gram in filterd_query])
		print(set_query)

		tmp_max = 0
		result = None
		for q in allquestion:

			question = q[1].rstrip().lower()
			question = ''.join(c for c in question if c not in punctuation)

			filterd_question = list(ngrams(question.split(), 1)) + list(ngrams(question.split(), 2))
			set_question = set([" ".join(gram).lower() for gram in filterd_question])

			ti_le = len(set_query & set_question) / len(set_question | set_query)

			if (ti_le >= tmp_max):
				tmp_max = ti_le
				result = q

		if(tmp_max == 0):
			return json.dumps({
				'status': 'fail',
				'content': None
			})
		return json.dumps({
			'status': 'success',
			'content': {
				'id': result[0],
				'question': result[1],
				'answer': result[2],
				'ti_le': tmp_max
			}
		})

