x = int(input(":"))
y = int(input(":"))

f = x%2 == 0 and y%2 != 0
s = y%2 == 0 and x%2!= 0
if(f or s):
	print("x : {0}, y : {1}, sum : {2}".format(x,y,(x+y)))
else:
	print("invalid input")
