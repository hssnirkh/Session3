sum = 0
counter = 0
avg = 0
for i in range(1,3):
	name = input("enter name : ")
	num = int(input("Tedad dars ha ra vared konid : "))
	sum = 0
	for j in range(1,num+1):
		grades = float(input("Grad {0} :".format(j)))
		sum+=grades
	avg = sum/num
	print(name,avg)
