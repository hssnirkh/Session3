num = int(input("Enter Num : "))
counter = 0
#mosavi naboodan
if(num % 2 == 0):
	num -= 1

while(num != 0):
	if(num % 2 == 0):
		counter +=1
		print(num)
#break point
	num -= 1
print("tedad argham zoj kochektar = {0}".format(counter))
