import numpy as np

PI = 3.1415926535897932385


def vec3(x, y, z):
	return np.array([x, y, z])

def vecLength(vector: np.array):
	return np.sqrt(lengthSquared(vector))


def lengthSquared(vector: np.array):
	return vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2]

def unitVector(vector: np.array):
	return vector / vecLength(vector)

def degreesToRadians(degrees):
	return degrees * PI / 180.0

def clamp(x, min, max):
	if(x < min):
		return min
	if(x > max):
		return max
	return x

def writeColor(fileStream, color: np.array, spp: float):

	fileStream.write("{} {} {}\n".format(color[0], color[1], color[2]))