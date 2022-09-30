import math
num = int(input("Enter num : "))
sq =int(math.sqrt(num))
 
if(num > 1):
	for i in range(2,sq + 1):
		if((num % i) == 0):
			print("NO {0} is not Prime num".format(num))
			break
	else:
		print("YES {0} is Prime num ".format(num))
else:
	print("no")
