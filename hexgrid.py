import math, functools

class HexGrid(object):
	def __init__(self, game, hexside = 15, width = 54, height = 30):
		self.game = game

		self.hexside = float(hexside)
		self.width = width
		self.height = height