from hittable import HitRecord
from hittable import Hittable
from material import Material
from ray import Ray
import numpy as np

class Sphere(Hittable):

	def __init__(self, center: np.array, radius: float, mat: Material):
		self.center = center
		self.radius = radius
		self.material = mat

	def hit(self, r: Ray, tMin, tMax, rec: HitRecord) -> bool:
		oc = r.origin() - self.center
		a = r.direction()
		a = np.power(np.linalg.norm(a), 2)
		halfB = np.dot(oc, r.direction())
		c = np.power(np.linalg.norm(oc), 2) - self.radius * self.radius
		discriminant = halfB * halfB - a*c

		if(discriminant < 0):
			return False

		# Find nearest root in acceptable range
		sqrtd = np.sqrt(discriminant)
		root = (-halfB - sqrtd) / a
		if(root < tMin or tMax < root):
			root = (-halfB + sqrtd) / a
			if(root < tMin or tMax < root):
				return False

		rec.t = root
		rec.point = r.at(rec.t)
		outwardNormal = (rec.point - self.center) / self.radius
		rec.setFaceNormal(r, outwardNormal)
		rec.material = self.material

		return True
