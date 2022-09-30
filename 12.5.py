a = input("A = ")
b = input("B = ")
countA ,countB = 0 ,0

for i in range(0,len(a)):
	if(ord(a[i]) > 47 and ord(a[i]) < 58):
		countA += 1
	else:
		countA = 0

for j in range(0,len(b)):
	if(ord(b[j]) > 47 and ord(b[j]) < 58):
		countB += 1
	else:
		countB = 0
print(countA,countB)
if((countA == len(a)) and (countB == len(b))):
	print("INT => {0} + {1} = {2}".format(a,b,int(a)+int(b)))
	print("INT => {0} * {1} = {2}".format(a,b,int(a)*int(b)))
else:
	print("STR => {0} + {1} = {2}".format(a,b,(a+b)))
