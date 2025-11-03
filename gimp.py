
class PPM:
	def __init__(self, size_x: int, size_y: int):
		self.size_x: int = size_x
		self.size_y: int = size_y
		self.pixels: list = []

	def load(self, filename: str):
		with open(filename, "r") as f:
			line1 = f.readline()
			if line1 != "P3":
				raise Exception("something went wrong, I can feel it")
			line2 = f.readline()
			if line2[0] == "#":
				line2 = f.readline()
			self.size_x = int(line2.split(" ")[0])
			self.size_y = int(line2.split(" ")[1])

			line3 = f.readline()
			if line3 != "255":
				raise Exception("something is wrong I can feel it")

			for i in range(self.size_x):
				self.pixels.append([])
				for j in range(self.size_y):
					self.pixels[i].append([])
					for color in range(3):
						c = int(f.readline())
						self.pixels[i][j].append(c)

	def write(self, filename: str):
		with open(filename, "w") as f:
			f.write("P3")
			f.write("# Created with Python")
			f.write(f"{self.size_x} {self.size_y}")
			f.write("255")
			for i in range(self.size_x):
				for j in range(self.size_y):
					for color in range(3):
						f.write(self.pixels[i][j][color])
