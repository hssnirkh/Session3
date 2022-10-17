m = int(input("m : "))
n = int(input("n : "))
#bozorgtarin maghsomalaie moshtarak b m m
def gcd(a,b):
	r = a % b
	if(r == 0):
		return b
	else:
		return gcd(b,r)
print("gcd is {0}".format(gcd(m,n)))
#kochektarin mazrab moshtarak k m m
def lcm(a,b):
	if(b == 0):
		return a
	else:
		return a * b /gcd(a,b)
print("lcm is {0}".format(lcm(m,n)))
