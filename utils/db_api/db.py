import sqlite3



class ActionWithDB():
	"""Управление базой данных"""
	def __init__(self):
		#this code is only for using with sqlite3
		self.conn= sqlite3.connect('data.db')
		self.cursor = self.conn.cursor()
		
