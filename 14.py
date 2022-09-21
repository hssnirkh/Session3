h = int(input("hour = "))
m = int(input("min = "))
s = int(input("sec = "))

if(h >= 0 and h < 24):
	if(m >= 0 and m < 60):
		if(s >= 0 and s < 60):
			print("Time is {0}:{1}:{2}".format(h,m,s))
		else:
			print("invalid sec")
	else:
		print("invalid min")
else:
	print("invalid hour")
