x = input("X : ")
y = input("Y : ")
num = ['0','1','2','3','4','5','6','7','8','9']
chr = ['a','s','d','f','g','h','j','k','l','q',\
'w','e','r','t','y','u','i','o','p','z','x','c',\
'v','b','n','m']
for i in range(0,9):
	if(num[i] in x):
		flag = True
		for j in range(0,26):
			if(chr[j] in x):
				flag = False
	else:
		continue
if (flag):
	print("x is INT")
else:
	print("x is STR")
# ta inja fahmidim x che type hast

for z in range(0,9):
        if(num[z] in y):
                flag = True
                for v in range(0,26):
                        if(chr[v] in y):
                                flag = False
        else:
                continue
if(flag):
        print("y is INT")
else:
	print("y is STR")

