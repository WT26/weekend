import numpy as np

class Ray:
	orig = np.array([])
	dir = np.array([])

	def __init__(self, orig = np.array([]), dir = np.array([])):
		self.orig = orig
		self.dir = dir

	def origin(self):
		return self.orig

	def direction(self):
		return self.dir

	def at(self, t):
		return self.orig + t * self.dir
