list = []
for i in range(1,21):
	name = input("{0}= Name : ".format(i))
	tedad = int(input("tedad dars : "))
	list.append(name)
	for j in range(1,tedad+1):
		grade = float(input("Enter Grade {0} : ".format(j)))
		if (grade > 15):
			list.append(grade)
print(list)
