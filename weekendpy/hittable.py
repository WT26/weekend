from utils import *
from ray import *
from material import *

class HitRecord:
	point = np.array([])
	normal = np.array([])
	t = 0.0
	frontFace = True
	material: Material

	def __init__(self, point = None, normal = None, t = None):
		self.point = point
		self.normal = normal
		self.t = t
		self.material = vec3(0.0, 0.0, 0.0)

	def setFaceNormal(self, ray: Ray, outwardNormal: np.array):
		self.frontFace = np.dot(ray.direction(), outwardNormal)
		self.normal = outwardNormal if self.frontFace else -outwardNormal

class Hittable():
	def hit(self, ray: Ray, tMin, tMax, rec: HitRecord) -> bool:
		raise NotImplementedError()