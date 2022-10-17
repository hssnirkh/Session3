#problem
#LCM
#Least common multiple
m = int(input("m : "))
n = int(input("n : "))

def cmList(num):
	mainList = []
	for i in range(1,num+1):
		mainList.append(num * i)
	return mainList
print(cmList(m),cmList(n))
def lcmList(m,n):
	aList = []
	for ii in range(1,len(m)+1):
		for jj in range(1,len(n)+1):
			if(m[ii] == n[jj]):
				aList.append(m[ii])
				#break
	return aList
print(lcmList(cmList(m),cmList(n)))
