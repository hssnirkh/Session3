sum = 0
c = 0
for i in range(1,21):
	name = str(input("Name : "))
	tedad = int(input("tedad dars ha : "))
	sum = 0
	for j in range(1, tedad+1):
		grade=float(input("grades : "))
		sum += grade
	avg = sum / tedad
	print("{0} moadel shoma {1}".format(name,avg))
	print(avg)
