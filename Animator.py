"""
ASCII Animator
"""
import os
import sys
import json
import threading
from time import sleep

class Animation:
	def __init__(self, frames, cfg):
		self._state = "stopped"
		self._frame = cfg["Start"]
		self._frames = frames
		self._duration = cfg["Duration"] or 1 / len(frames)

	def play(self, playCount=1):
		if playCount > 0:
			self._state = "playing"
			loopCount = 0

			def count(loopCount):
				if self._state == "playing":
					os.system("cls")
					print(self._frames[self._frame])
					sleep(self._duration)

					if self._frame < len(self._frames) - 1:
						self._frame = self._frame + 1
						t1 = threading.Thread(target=count, args=[loopCount])
						t1.start()
					else:
						self._frame = 0
						loopCount = loopCount + 1
						if loopCount < playCount:
							t1 = threading.Thread(target=count, args=[loopCount])
							t1.start()
						else:
							self._state = "stopped"

			t1 = threading.Thread(target=count, args=[loopCount])
			t1.start()
		else:
			self._state = "playing"

			def count():
				if self._state == "playing":
					os.system("cls")
					print(self._frames[self._frame])
					sleep(self._duration)

					if self._frame < len(self._frames) - 1:
						self._frame = self._frame + 1
					else:
						self._frame = 0

					count()

			t1 = threading.Thread(target=count, args=[])
			t1.start()

	def pause(self):
		if self._state == "playing":
			self._state = "paused"

	def stop(self):
		if self._state == "playing" or self._state == "paused":
			self._frame = 0
			self._state = "stopped"

	def reverse(self):
		self._frames.reverse()

def load(file):
	file = open(file, "r")
	data = file.readlines()
	file.close()

	cfg = json.loads(data[0])
	data.remove(data[0])

	data = "".join(data)
	data = data.split("-")

	for i in range(len(data)):
		if data[i][0:1] == "\n":
			data[i] = data[i][1:]

	return Animation(data, cfg)