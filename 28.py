num = int(input("enter num: "))

def intPow2(num):
	c = 0
	counter = 0
	sum = 0
	while(c != num):
		if(counter % 2 != 0):
			c += 1
			sum += counter
		counter += 1

	return counter , sum
print(intPow2(num))
