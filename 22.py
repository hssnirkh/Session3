while(True):
	print("TYPE 0 for exit")
	num = float(input("PLS Enter Number: "))
	if(num == 0):
		break
	elif(num % 2 == 0 and num % 3 == 0):
                print("Yes {0} mod by 3 and 2 is 0 .".format(num))
	else:
		print("Try Another Number !")
