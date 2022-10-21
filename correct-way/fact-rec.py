def fact_rec(num):
	if(num == 1):
		return 1
	else:
		return num * fact_rec(num-1)

print(fact_rec(int(input())))
