x = input("X : ")
y = input("Y : ")
print()
num = ['0','1','2','3','4','5','6','7','8','9']
chr = ['a','s','d','f','g','h','j','k','l','q',\
'w','e','r','t','y','u','i','o','p','z','x','c',\
'v','b','n','m']
flag = False
xIs = 0
yIs = 0

for i in range(0,9):
        if(num[i] in x):
                flag = True
        else:
                continue
for j in range(0,26):
	if(chr[j] in x):
		flag = False
#Check x is int or str
if (flag):
	print("x is INT")
	xIs+=1
else:
        print("x is STR")
# ta inja fahmidim x che type hast

for z in range(0,9):
        if(num[z] in y):
                flag = True
        else:
                continue

for v in range(0,26):
	if(chr[v] in y):
		flag = False
#check y is int or str
if(flag):
	print("y is INT")
	yIs+=1
else:
        print("y is STR")
# ta inja fahmidam y che type hast

if((xIs == 1) and (yIs ==1)):   #int+int
	print("int + int = {0}".format(int(x)+int(y)))
	print("int * int = {0}".format(int(x)*int(y)))
elif((xIs ==1) and (yIs ==0)):   #int+str
	print("int + str = {0}".format(x+y))
elif((xIs ==0) and (yIs ==1)):   #str+int
        print("str + int = {0}".format(x+y))
else:                            #str+str
	print("str + str = {0}".format(x+y))
