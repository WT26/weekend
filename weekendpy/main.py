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

def rayColor(r: Ray) -> np.array:
	unitDir = unitVector(r.direction())
	t = 0.5 * (unitDir[0, 1] + 1.0)
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

	origin = vec3(0, 0, 0)
	horizontal = vec3(viewPortWidth, 0, 0)
	vertical = vec3(0, viewPortHeight, 0)
	lowerLeftCorner = origin - horizontal/2 - vertical/2 - vec3(0, 0, focalLength)


	# Render
	imgFile = open("image.ppm", "w")

	imgFile.write("P3\n{} {}\n255\n".format(width, height))

	for j in range(height):
		for i in range(width):
			u = i / (width - 1)
			v = j / (height - 1)
			r = Ray(origin, lowerLeftCorner + u * horizontal + v * vertical - origin)
			rgb = rayColor(r)
			#rgb = np.array([[u, v, 0.2]])
			writeColor(imgFile, rgb)



	imgFile.close()
