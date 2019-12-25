a=int(input("enter a palindrome number:"))
print("original palindrome number:",a)
b=a
r=0
while a>0:
	c=a%10
	r=r*10+c
	a=a//10
if(b==r):
    print("reversed palindrome number",b)
else:
    print("not a palindrme")