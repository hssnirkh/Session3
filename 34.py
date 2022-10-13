#bug

for i in range(100,1000):
	s = str(i)

	for j in range(0,len(s)):
		if(s[j] == '0'):
			break
			print("OK{0}".format(i))
	print("S")
