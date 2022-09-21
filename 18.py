num = int(input("Pls Enter Num : "))
counter = 0
sum = 0
#check mosavi naboodan
if(num % 2 ==1):
	num -= 1

while(num != 0):
	if(num % 2 == 1):
		counter += 1
		sum += num
#break point
	num -= 1
print("tedad argham fard kamtar = {0}".format(counter))
print("majmo adad fard kochektar = {0}".format(sum))
