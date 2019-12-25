def marks(arg1,arg2,arg3,arg4,arg5):
	print("eng marks:",arg1)
	print("math marks:",arg2)
	print("sci marks:",arg3)
	print("tamil marks:",arg4)
	print("soc marks:",arg5)
	total=arg1+arg2+arg3+arg4+arg5
	print("total is:",total)
	average=total/5
	print("average is",average)
	return;
    
arg1=int(input("enter  eng marks:"))
arg2=int(input("enter  math marks:"))
arg3=int(input("enter  sci marks:"))
arg4=int(input("enter  tamil marks:"))
arg5=int(input("enter  soc marks:"))
marks(arg1,arg2,arg3,arg4,arg5)