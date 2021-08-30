import numpy as np

def vec3(x, y, z):
	return np.array([[x, y, z]])

def writeColor(fileStream, color):
	ir = int(255.999 * color[0, 0])
	ig = int(255.999 * color[0, 1])
	ib = int(255.999 * color[0, 2])

	fileStream.write("{} {} {}\n".format(ir, ig, ib))
