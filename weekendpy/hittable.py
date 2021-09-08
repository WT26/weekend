from utils import *
from ray import *

class HitRecord:
	point = np.array([])
	normal = np.array([])
	t = 0.0
	frontFace = True

	def __init__(self, point = None, normal = None, t = None):
		self.point = point
		self.normal = normal
		self.t = t

	def setFaceNormal(self, ray: Ray, outwardNormal: np.array):
		self.frontFace = np.dot(ray.direction(), outwardNormal)
		self.normal = outwardNormal if self.frontFace else -outwardNormal

class Hittable():
	def hit(self, ray: Ray, tMin, tMax, rec: HitRecord) -> bool:
		raise NotImplementedError()