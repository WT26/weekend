import numpy as np
from utils import *
from ray import Ray

class Camera:
	origin = np.array([])
	horizontal = np.array([])
	vertical = np.array([])
	lowerLeftCorner = np.array([])

	def __init__(self, aspectRatio):
		viewPortHeight = 2.0
		viewPortWidth = aspectRatio * viewPortHeight
		focalLength = 1.0

		self.origin = vec3(0.0, 0.0, 0.0)
		self.horizontal = vec3(viewPortWidth, 0.0, 0.0)
		self.vertical = vec3(0.0, viewPortHeight, 0.0)
		self.lowerLeftCorner = self.origin - self.horizontal/2.0 - self.vertical/2.0 - vec3(0.0, 0.0, focalLength)

	def getRay(self, u: float, v: float):
		return Ray(self.origin,
					self.lowerLeftCorner + u*self.horizontal + v*self.vertical - self.origin);
