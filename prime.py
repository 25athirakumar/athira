a=int(input("enter number:"))
if a > 0:
	for i in range (2,a):
        if (a % i ==0):
            print("not a prime number")
            break
        else:
        print("it is a prime number")
