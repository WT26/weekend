#from hittable import HitRecord
from ray import *
from utils import *
import numpy as np

class Material():
	def scatter(self, rayIn: Ray, rec, attenuation: np.array, scattered: Ray) -> bool:
		raise NotImplementedError()

class Lambertian(Material):
	albedo: np.array = np.array([1.0, 0.0, 1.0])

	def __init__(self, color: np.array):
		self.albedo = color

	def scatter(self, rayIn: Ray, rec, attenuation: np.array, scattered: Ray) -> bool:
		scatterDirection = rec.normal + randomUnitVector()

		if(nearZero(scatterDirection)):
			scatterDirection = rec.normal

		scattered.orig = rec.point
		scattered.dir = scatterDirection
		attenuation[0] = self.albedo[0]
		attenuation[1] = self.albedo[1]
		attenuation[2] = self.albedo[2]
		return True

class Metal(Material):
	albedo: np.array = np.array([1.0, 0.0, 1.0])
	fuzz : float = 1.0

	def __init__(self, color: np.array, fuzz: float):
		self.albedo = color
		self.fuzz = fuzz if fuzz < 1.0 else 1.0

	def scatter(self, rayIn: Ray, rec, attenuation: np.array, scattered: Ray) -> bool:
		reflected = reflect(unitVector(rayIn.direction()), rec.normal)
		scattered.orig = rec.point
		scattered.dir = reflected + self.fuzz * randomInUnitSphere()
		attenuation[0] = self.albedo[0]
		attenuation[1] = self.albedo[1]
		attenuation[2] = self.albedo[2]
		return (np.dot(scattered.direction(), rec.normal) > 0)
