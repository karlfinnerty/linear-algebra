from Vector import Vector
from input_components import components

def main():

	x1, y1, z1 = components()
	x2, y2, z2 = components()
	u = Vector(x1, y1, z1)
	v = Vector(x2, y2, z2)

	alpha, P = u.proof_1(v)
	print("alpha: {}, P: {}".format(alpha, P))

if __name__ == '__main__':
	main()