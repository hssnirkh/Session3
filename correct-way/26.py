#simple way
num = int(input("enter num: "))
mpy = 1
for i in range(1,num+1):
	mpy*=i
print(mpy)

#def way
def factor(num):
	fac = 1
	for j in range(1,num+1):
		fac*=j
	return fac
print(factor(num))

#Recersive Way
def fact_rec(num):
	if(num == 1):
		return 1
	else:
		return num * fact_rec(num-1)
print(fact_rec(num))
