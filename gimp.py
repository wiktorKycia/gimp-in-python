
class PPM:
	def __init__(self, size_x: int, size_y: int):
		self.size_x = size_x
		self.size_y = size_y
		self.pixels = []

	def load(self, filename: str):
