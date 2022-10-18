num = int(input("adad : "))
paye = int(input("paye : "))

def log_rec(n,p):
	r = n / p
	s = 1
	if(r == 1):
		return s
	else:
		return s + log_rec(r,p)
print(log_rec(num,paye))

