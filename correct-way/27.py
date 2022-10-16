#simple way
num = int(input("enter num: "))
#def way
def fibo(num):
	a = 0
	b = 1
	if(num<=2):
		return b
	else:
		for i in range(1,num):
			c = a + b
			a = b
			b = c
		return b
print(fibo(num))
#Recursive Way
def fibo_rec(num):
	if(num<=2):
		return 1
	else:
		return fibo_rec(num - 2) + fibo_rec(num - 1)
print(fibo_rec(num))
