import math



def fun(x):
	return 2*math.sin(0.9*x)-math.tan(x)

def bise(a,b):
	if(fun(a)*fun(b)>=0):
		print("you have not assumed right value a and b \n")
		return
	c=a
	while((b-a)>=0.01):

		c=(a+b)/2 #find the middle point
#check if middle point is root
		if(fun(c)==0.0):
			break
#decide the side to repeat the steps
		if(fun(c)*fun(a)<0):
			b=c
		else:
			a=c
	print("the value of root is : ","%.4f"%c)


a=float(input("guess the 1st req solition in interval"))
b=float(input("guess the 2nd req solition in interval"))

bise(a,math.pi/2)

