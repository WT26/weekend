import sys
import argparse
import numpy as np
from utils import *

def cmdline_args():
	p = argparse.ArgumentParser(add_help=False)


	p.add_argument("-w", "--width", type=int, default=520,
					help="output screen width")

	p.add_argument("-h", "--height", type=int, default=520,
					help="output screen height")

	return(p.parse_args())

if __name__ == '__main__':
	args = cmdline_args()
	print(args)

	# Image
	width = args.width
	height = args.height

	# Render
	imgFile = open("image.ppm", "w")

	imgFile.write("P3\n{} {}\n255\n".format(width, height))

	for j in range(height, 0, -1):
		for i in range(width):
			rgb = np.array([[i / (width - 1), j / (height - 1), 0.2]])
			writeColor(imgFile, rgb)



	imgFile.close()
