import numpy as np

def vec3(x, y, z):
	return np.array([x, y, z])

def unitVector(vector: np.array):
	norm=np.linalg.norm(vector, ord=1)
	if norm==0:
		norm=np.finfo(vector.dtype).eps
	return vector/norm



def writeColor(fileStream, color: np.array):
	ir = int(255.999 * color[0])
	ig = int(255.999 * color[1])
	ib = int(255.999 * color[2])

	fileStream.write("{} {} {}\n".format(ir, ig, ib))
