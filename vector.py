import math

class Vector():

	#initialize vector by inputting parameters
	def __init__(self, x, y, z = None):
		self.x = x
		self.y = y

		if z == None:
			self.z = 0
		else:
			self.z = z

	def get(self):
		return self.x, self.y, self.z

	def set(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def add(self, other):
		x = self.x + other.x
		y = self.y + other.y
		z = self.z + other.z
		new = Vector(x, y, z)
		return new

	def sub(self, other):
		x = self.x - other.x
		y = self.y - other.y
		z = self.z - other.z
		new = Vector(x, y, z)
		return new

	#multiplies a vector by a scalar
	def mult(self, n):
		x = self.x * n
		y = self.y * n
		z = self.z * n
		new = Vector(x, y, z)
		return new

	def magnitude(self):
		return math.sqrt((self.x)**2 + (self.y)**2 + (self.z)**2)

	def dot(self, other):
		x = self.x * other.x
		y = self.y * other.y
		z = self.z * other.z
		return x + y + z

	def cross(self, other):
		x = self.x * other.x
		y = self.y * other.y
		z = self.z * other.z
		new = Vector(x, y, z)
		return new	

	#return angle between two vectors
	def v_angle(self, other):
		theta = self.dot(other)/(self.magnitude() * other.magnitude())
		theta = round(theta, 3)
		return round(math.degrees(math.acos(theta)), 3)

	#method gets solution to proof  (v = xu + P)  where vectors u and v are given, and P is perpendicular to u
	#treat self as vector u, and other as vector v
	def proof_1(self, other):
		x = self.dot(other)/self.dot(self)
		P = other.sub(self.mult(x))
		return x, P

	def is_unit_vector(self):
		if round(self.magnitude(), 3) == 1:
			return True
		else:
			return False

	def is_orthogonal(self, other):
		if self.dot(other) == 0:
			return True
		else:
			return False

	def is_orthonormal(self, other):
		if self.is_orthogonal(other) == True and(self.is_unit_vector() and other.is_unit_vector()) == True:
			return True
		else:
			return False

	def __str__(self):
		return "{}, {}, {}".format(self.x, self.y, self.z)