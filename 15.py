import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
delta = math.pow(b,2)-(4*a*c)
print(delta)
if (delta > 0):
	x1 = (-b + math.sqrt(delta))/(2 * a)
	x2 = (-b - math.sqrt(delta))/(2 * a)
	print(x1,x2)
elif (delta == 0):
	x = b / 2 * a
	print(x)
else:
	print("not Found")
