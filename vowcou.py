vowels=0
str1=input("enter string ")
a=e=i=o=u=0
for i in str1:
    if(i == 'a' or i == 'A'):
        a=a+1
        print("char ",i)
        print("a= ",a)
    elif (i == 'e' or i == 'E'):
        e=e+1
        print("char ",i)
        print("e= ",e)
    elif (i == 'i' or i == 'I'):
        u=u+1
        print("char ",i)
        print("i= ",i)
    elif (i == 'o' or i == 'O'):
        o=o+1
        print("char ",i)
        print("0= ",o)
    elif (i == 'u' or i == 'U'):
        u=u+1
        print("char ",i)
        print("u= ",u)
    