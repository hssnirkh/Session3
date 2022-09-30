import math
num = int(input("Enter num : "))
sq =int(math.sqrt(num))

if(num > 3):
	for i in range(2,sq + 1):
		if((num % i) == 0):
			print("NO {0} is not Prime num".format(num))
			break
	else:
		print("YES {0} is Prime num ".format(num))
"""
elif((num == 2) or (num == 3)):
	print("yes {0} is Prime num ".format(num))
elif(num == 1):
	print("NO {0} is Exception".format(num))
"""
