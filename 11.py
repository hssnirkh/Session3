a = int(input())
b = int(input())
c = int(input())
#fisaghoores baraie ghaem ol zavie
if(((a**2)==(b**2)+(c**2)) or ((b**2) == (c**2)+(a**2)) or ((c**2) == (a**2)+(b**2))):
	print("ghaem")
#mosavi azla
elif(a==b and b==c):
	print("mosavi azla")
#motesavi al saghein
elif(a==b or b==c):
	print("mosavi saghein")

else:
	print("not found")
