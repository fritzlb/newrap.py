import math

def x_next(x):
	fkt = (x-5)*math.exp(x)+5
	dev = (x-4)*math.exp(x)
	ret = -fkt/dev + x
	return ret

epsilon = 1E-6

prev = 0
cur = 10

while abs(cur-prev) > epsilon:
	prev = cur
	cur = x_next(prev)

print(cur)

