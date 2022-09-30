n = int(input("Enter N : "))
m = int(input("Enter M : "))
s = 1
BMM = 1
nList = []
mList = []

#appending Div in list
for i in range(1,n+1):
	if(n % i == 0):
		nList.append(i)
print(nList)
for j in range(1, m+1):
	if(m % j == 0):
		mList.append(j)
print(mList)
if (n > m):
	s = m
else:
	s = n

for z in range(1, s+1):
	if((n % z == 0) and (m % z == 0)):
		BMM = z
print("BMM = " ,BMM)
