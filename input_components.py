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