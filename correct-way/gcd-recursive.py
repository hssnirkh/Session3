m = int(input("m : "))
n = int(input("n : "))
#print(m % n)
def gcd_rec(m,n):
	d = m % n
	if(d == 0):
		return n
	else:
		return gcd_rec(n,d)
print(gcd_rec(m,n))
