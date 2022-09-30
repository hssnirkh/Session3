num = int(input("Enter num : "))
list = []

while(num != 0):
	c = num % 10
	num //= 10
	list.append(c)

list.reverse()
print(list)
