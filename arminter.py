s = int(input("Enter a number: "))
l = int(input("Enter a number: "))
sum = 0
for i in range (s,l+1):
    temp = i
	while temp >0:
		digit = temp % 10
		sum = sum + digit ** 3
		temp = temp//10
if i == sum:
   print(i,"is an Armstrong number")
else:
   print(i,"is not an Armstrong number")
