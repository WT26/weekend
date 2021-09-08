import threading
import numpy as np






class ImageContext():
	def __init__(self, width, height):
		self.lock = threading.Lock()
		self.listOfRgbs = np.zeros((height, width, 3))
		self.counter = 0
		self.scanLines = height


	def addNewSample(self, newSample: np.array, j: int):
		self.lock.acquire()

		try:
			self.listOfRgbs[j-1] = newSample
			self.counter += 1
			print("Progress: ", self.scanLines - self.counter, "/", self.scanLines, end = "\r")
		finally:
			self.lock.release()
