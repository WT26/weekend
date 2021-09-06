import ctypes
from math import inf, radians
import sys
import argparse
import threading
import numpy as np
import random
import copy

from numpy.core.fromnumeric import reshape
from ray import Ray
from sphere import Sphere
from utils import *
from hittable import Hittable
from hittable import HitRecord
from hittableList import HittableList
from camera import Camera
from imageContext import ImageContext
import multiprocessing as mp


def cmdline_args():
	p = argparse.ArgumentParser(add_help=False)


	p.add_argument("-w", "--width", type=int, default=520,
					help="output screen width")

	p.add_argument("-h", "--height", type=int, default=520,
					help="output screen height")

	return(p.parse_args())

def rayColor(r: Ray, world: Hittable) -> np.array:
	hitRecord = HitRecord()
	if(world.hit(r, 0, inf, hitRecord)):
		return 0.5 * (hitRecord.normal + vec3(1.0, 1.0, 1.0))

	unitDir = unitVector(r.direction())
	t = 0.5 * (unitDir[1] + 1.0)
	return (1.0 - t) * vec3(1.0, 1.0, 1.0) + t * vec3(0.5, 0.7, 1.0)

def rayTrace(width, height, scanLine, spp, cam, world, imageContext):
	rgbSlice = np.zeros((width, 3))
	for i in range(width):
		colorSum = vec3(0.0, 0.0, 0.0)
		for s in range(spp):
			u = (float(i) + random.uniform(0.0, 0.999999))/float(width)
			v = (float(j) + random.uniform(0.0, 0.999999))/float(height)
			r = cam.getRay(u, v)
			colorSum += rayColor(r, world)
		rgbSlice[i] = colorSum

	imageContext.addNewSample(rgbSlice, scanLine)

if __name__ == '__main__':
	args = cmdline_args()
	print(args)

	# Image
	width = 400
	aspectRatio = 16.0 / 9.0
	height = int(width / aspectRatio)
	spp = 16

	# World
	world = HittableList()
	world.add(Sphere(vec3(0, 0, -1), 0.5))
	world.add(Sphere(vec3(0, -100.5, -1), 100))

	# Camera
	cam = Camera(aspectRatio)


	# Render
	imgFile = open("image.ppm", "w")

	imgFile.write("P3\n{} {}\n255\n".format(width, height))

	imageContext = ImageContext(width, height)

	multiThread = False
	if(multiThread):
		threads = []
		for j in range(height, 0, -1):
			t = threading.Thread(name=f'j: {j}', target=rayTrace, args=(width, height, copy.deepcopy(j), spp, cam, world, imageContext,))
			t.start()
			threads.append(t)

		for t in threads:
			t.join()
	else:
		for j in range(height, 0, -1):
			rayTrace(width, height, j, spp, cam, world, imageContext)

	reshaped = imageContext.listOfRgbs.reshape(width*height, 3)
	reshaped = int(255.999) * reshaped
	scale = 1.0 / spp
	reshaped = reshaped * scale
	reshaped = np.flipud(reshaped)
	for rgb in reshaped:
		writeColor(imgFile, rgb, spp)


	imgFile.close()


