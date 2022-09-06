#firstWay
num = float(input("PLS Enter Value : "))

checker = num - int(num)
if(checker != 0):
	print("intiger shode = {0}".format(int(num)))
else:
	print("PLS Enter Float number")

#SecondWay
num = float(input("PLS Enter Value 2: "))
if(num/2 != num//2):
        print("intiger shode = {0}".format(int(num)))
else:
        print("PLS Enter Float number")
