x = input()
y = input()
num = ['0','1','2','3','4','5','6','7','8','9']
chr = ['a','s','c','d','e','f','g','r','q','z','w','e','x','c','v']
j = 0
c = 0
for i in num:
	if(num[j] in x):
		for z in chr:
			if(chr[c] not in x):
				print(x)
			c+=1
	j+=1
