from math import radians
import sys
import argparse
from ray import Ray
import numpy as np
from utils import *

def cmdline_args():
	p = argparse.ArgumentParser(add_help=False)


	p.add_argument("-w", "--width", type=int, default=520,
					help="output screen width")

	p.add_argument("-h", "--height", type=int, default=520,
					help="output screen height")

	return(p.parse_args())

def hitSphere(center: np.array, radius: float, r: Ray) -> bool:
	oc = r.origin() - center
	a = r.direction()
	a = np.power(np.linalg.norm(a), 2)
	halfB = np.dot(oc, r.direction())
	c = np.power(np.linalg.norm(oc), 2) - radius * radius
	discriminant = halfB * halfB - a*c

	if(discriminant < 0):
		return -1.0
	else:
		return (-halfB - np.sqrt(discriminant)) / a

def rayColor(r: Ray) -> np.array:
	t = hitSphere(vec3(0.0, 0.0, -1.0), 0.5, r)

	if(t > 0.0):
		N = unitVector(r.at(t) - vec3(0, 0, -1))
		return 0.5 * vec3(N[0] + 1.0, N[1] + 1.0, N[2] + 1.0)

	unitDir = unitVector(r.direction())
	t = 0.5 * (unitDir[1] + 1.0)
	return (1.0 - t) * vec3(1.0, 1.0, 1.0) + t * vec3(0.5, 0.7, 1.0)

if __name__ == '__main__':
	args = cmdline_args()
	print(args)

	# Image
	width = 400
	aspectRatio = 16.0 / 9.0
	height = int(width / aspectRatio)


	# Camera
	viewPortHeight = 2.0
	viewPortWidth = aspectRatio * viewPortHeight
	focalLength = 1.0

	origin = vec3(0.0, 0.0, 0.0)
	horizontal = vec3(viewPortWidth, 0.0, 0.0)
	vertical = vec3(0.0, viewPortHeight, 0.0)
	lowerLeftCorner = origin - horizontal/2.0 - vertical/2.0 - vec3(0.0, 0.0, focalLength)


	# Render
	imgFile = open("image.ppm", "w")

	imgFile.write("P3\n{} {}\n255\n".format(width, height))
	listOfRgbs = []
	for j in range(height, 0, -1):
		for i in range(width):
			u = float(i)/float(width)
			v = float(j)/float(height)
			r = Ray(origin, lowerLeftCorner + u * horizontal + v * vertical - origin)
			rgb = rayColor(r)
			listOfRgbs.append(rgb)
			#rgb = np.array([[u, v, 0.2]])


		print("Progress: ", height - j, "/", height, end = "\r")
	for rgb in listOfRgbs:
		writeColor(imgFile, rgb)


	imgFile.close()
