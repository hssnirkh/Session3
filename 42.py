num = int(input("Enter Num: "))
sum = 0 
for i in range(1, num):
	if(num % i == 0):
		sum+=i
if(sum == num):
	print("Tam Ya Kamel")
else:
	print("no")
