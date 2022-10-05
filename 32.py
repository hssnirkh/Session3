num = int(input("Enter Num: "))
sum = 0
while(num != 0):
	c=num % 10
	if(c % 2 == 0):
		sum += c
		#print(c)
	num //=10
print("sum = ",sum)
