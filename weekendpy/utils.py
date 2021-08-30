import numpy as np

def vec3(x, y, z):
	return np.array([x, y, z])

def vecLength(vector: np.array):
	return np.sqrt(lengthSquared(vector))


def lengthSquared(vector: np.array):
	return vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2]


def unitVector(vector: np.array):
	return vector / vecLength(vector)



def writeColor(fileStream, color: np.array):
	ir = int(255.999 * color[0])
	ig = int(255.999 * color[1])
	ib = int(255.999 * color[2])

	fileStream.write("{} {} {}\n".format(ir, ig, ib))
