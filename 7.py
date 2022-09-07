x = int(input("sec: "))
y = int(input("min: "))

minToSec = y * 60
if(x > minToSec):
	print("sec")
elif(minToSec > x):
	print("min")
else:
	print("invalid")
