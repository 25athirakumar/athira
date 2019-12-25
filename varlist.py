def value(a1,*varlist):
	print  ("out",a1)
	for var in varlist:
		print (var)
	return;
value(10)
value(35,45,55)