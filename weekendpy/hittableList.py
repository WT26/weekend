from typing import Tuple
from hittable import Hittable
from hittable import HitRecord
from ray import Ray

class HittableList(Hittable):
	objects = []

	def __init__(self, objects = []):
		self.objects = objects

	def clear(self):
		objects = []

	def add(self, object: Hittable):
		self.objects.append(object)

	def hit(self, ray: Ray, tMin, tMax, rec: HitRecord) -> bool:
		tempRecord = HitRecord()
		hitAnything = False;
		closestSoFar = tMax;

		for obj in self.objects:
			if(obj.hit(ray, tMin, closestSoFar, tempRecord)):
				rec.normal = tempRecord.normal
				rec.point = tempRecord.point
				rec.t = tempRecord.t
				rec.frontFace = tempRecord.frontFace
				hitAnything = True
				closestSoFar = tempRecord.t

		return hitAnything;
