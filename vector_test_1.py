import Vector

def components():
	a = []
	print("Please enter 3 digits to initialize the vector (if the vector has only 2 components, enter third input as 0).")
	n = input()
	while n != '' and len(a) < 3:
		a.append(float(n))
		n = input()

	if len(a) == 3:
		z = a[2]
	y = a[1]
	x = a[0]

	return x, y, z

def main():

	x1, y1, z1 = components()
	x2, y2, z2 = components()

	u = Vector.Vector(x1, y1, z1)
	print("u: {}".format(u))

	v = Vector.Vector(x2, y2, z2)
	print("v: {}".format(v))

	print("|u|: {}".format(u.magnitude()))
	print("|v|: {}".format(v.magnitude()))

	print("u.v: {}".format(u.dot(v)))

	print("angle between u and v: {} degrees".format(u.v_angle(v)))


if __name__ == '__main__':
	main()
