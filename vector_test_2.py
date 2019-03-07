from Vector import Vector
from input_components import components

# the purpose of this program is to test the class set and get methods
def main():

	x, y, z = components()
	u = Vector(x, y, z)

	print(u.get())

	print("set new components")
	x, y, z = components()
	u.set(x, y, z)
	print(u.get())

if __name__ == '__main__':
	main()