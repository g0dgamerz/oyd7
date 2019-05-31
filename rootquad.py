from math import sqrt

print("quadratic function: (a*x^2)+b*x+c ")

a=int(input("Please enter value of cofficient a:"))
b=int(input("please enter value of cofficient b:"))
c=int(input("please enter value of cofficient c:"))

if a==0:
	print("cofficient a cannot be zero")
	exit()
d=b*b-4*a*c
sqrt_val=sqrt(abs(d))

if d>0:
	print("roots are real and different")
	x1=(-b+sqrt_val)/(2*a)
	x2=(-b-sqrt_val)/(2*a)
	print("the 2 roots are x1= %f and x2= %f" %(x1,x2))
elif d==0:
	x=(-b/(2*a))
	print("there is only one root:",x)
else: 
	print("no real root exists")
	exit()