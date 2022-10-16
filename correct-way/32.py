numm = num = int(input("enter num : "))
#simple Way
sum = 0
while(num != 0):
	c=num % 10
	if(c % 2 == 0):
		sum += c
	num //= 10
print(sum)

#recursive Way
def zoj(number):
	s = 0
	if(number <= 0):
		return 0
	else:
		if((number % 10) % 2 == 0):
			s = number % 10
		return s + zoj(number // 10)
print(zoj(numm))
