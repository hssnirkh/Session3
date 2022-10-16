import math
num = int(input("enter num: "))
#simple way
counter = 0
for i in range(1,num+1):
	if(num % i == 0):
		counter += 1
if(counter == 2):
	print("yes")
else:
	print("no")
#best Way
c = 0 
for j in range(1,int(math.sqrt(num)+1)):
	if(num % j == 0):
		c += 1
if(c == 1):
	print("yes")
else:
	print("no")
