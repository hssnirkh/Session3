def pow(a,p):
	if(p == 1):
		return a
	else:
		return a*pow(a,p-1)

num = int(input("adad : "))
poww = int(input("tavan : "))

print(pow(num,poww))
