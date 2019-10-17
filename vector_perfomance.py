from vector import Vector

import time
start = time.time()

def main():

	u = Vector(-1, 0, 2)

	v = Vector(3, 1, 1)

	u.magnitude()
	v.magnitude()

	dot = u.dot(v)

	angle = u.v_angle(v)

	u = Vector(1, -1, 2)
	v = Vector(2, 1, 1)

	alpha, P = u.proof_1(v)


if __name__ == '__main__':
	for i in range(0, 1000):
		main()
		i += 1

end = time.time()
print("executed {} times".format(i))
print("execution time: {}".format(end - start))
print("average execution time: {}".format((end - start)/i))
