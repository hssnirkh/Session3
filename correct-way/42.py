num = int(input("enter num: "))
sum = 0
for i in range(1,num):
	if(num % i == 0):
		sum += i
if(num == sum):
	print("tam")
elif(sum == 1):
	print("aval")
else:
	print("no")
