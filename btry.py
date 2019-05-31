import math
def samesign(a,b):
	return a*b >0

def bisect(func,low,high):
	assert not samesign(func(low),func(high))

	for i in range(50):
		midpoint=(low + high)/2.0
		if samesign(func(low),func(midpoint)):
			low=midpoint
		else:
			high=midpoint
	return midpoint

def f(x):
	return 2*math.sin(0.9*x)-math.tan(x)

x=bisect(f,0,math.pi/2)
print(x, f(x))