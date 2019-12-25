a=int(input("enter number:"))
b=int(input("enter number:"))
print("1.add 2.sub 3.mul 4.div 5.mod")
c=int(input("enter the operation to br performed:"))
print("value of a:",a)
print("value of b:",b)
if c==1:
	d=a+b
	print("add value ",d)
break;
etm
-lif c==2:
	e=a-b
	print("sub value ",e)
break;
elif c==3:
	f=a*b
	print("mul value ",f)
break;
elif c==4:
	g=a/b
	print("div value ",g)
break;
else:
	h=a%b
	print("mod value ",h)
	