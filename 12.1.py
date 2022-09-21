x = input()
y = input()
num = ['0','1','2','3','4','5','6','7','8','9']
j = 0
c = 0
for i in num:
	if(num[j] in x,y):
		print("int")
		print("{0} + {1} = {2}".format(x,y,(int(x)+int(y))))
		print("{0} * {1} = {2}".format(x,y,(int(x)*int(y))))
		break
	j+=1
