#Greatest Common Divisior
#GCD

m = int(input("m : "))
n = int(input("n : "))
#peida kardan maghsomalaie dar list
def cdList(num):
	mainList = []
	for i in range(1,num+1):
		if(num % i == 0):
			mainList.append(i)
	return mainList
#peida kardan bozorgtarin maghsomalaie dar list
def gcd(x,y):
	analogyList = []
	if(len(x) > len(y)):
		for i in range(0,len(y)):
			for j in range(0,len(x)):
				if(y[i] == x[j]):
					analogyList.append(y[i])
	elif(len(y) > len(x)):
		for ii in range(0,len(x)):
			for jj in range(0,len(y)):
				if(x[ii] == y[jj]):
					analogyList.append(x[ii])
	else:
		for iii in range(0,len(x)):
			for jjj in range(len(y)):
				if(x[iii] == y[jjj]):
					analogyList.append(x[iii])
	return analogyList


print(cdList(m),cdList(n))
#peida karedan max dar gcd
#print("GCD : {0}".format(max(gcd(cdList(m),cdList(n)))))

#short codding way
def gcd2(x,y):
	list = []
	for z in range(0,len(x)):
		for c in range(0,len(y)):
			if(x[z] == y[c]):
				list.append(x[z])
	return list
print("GCD : {0}".format(max(gcd2(cdList(m),cdList(n)))))

