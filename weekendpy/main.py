import sys
import argparse

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
			r = i / (width - 1)
			g = j / (height - 1)
			b = 0.25

			ir = int(255.999 * r)
			ig = int(255.999 * g)
			ib = int(255.999 * b)

			imgFile.write("{} {} {}\n".format(ir, ig, ib))

	imgFile.close()

#	for (int j = height-1; j >= 0; --j) {
#		for (int i = 0; i < image_width; ++i) {
#			auto r = double(i) / (image_width-1);
#			auto g = double(j) / (image_height-1);
#			auto b = 0.25;
#
#			int ir = static_cast<int>(255.999 * r);
#			int ig = static_cast<int>(255.999 * g);
#			int ib = static_cast<int>(255.999 * b);
#
#			std::cout << ir << ' ' << ig << ' ' << ib << '\n';
#		}
#	}
