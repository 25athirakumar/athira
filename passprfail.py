mark1=float(input("enter english mark:"))
mark2=float(input("enter maths mark:"))
mark3=float(input("enter science mark:"))
mark4=float(input("enter social mark:"))
total=mark1+mark2+mark3+mark4
average=(total/200) *100
if(mark1 >=25 and mark2 >=25 and mark3 >=25 and mark4 >=25):
    print("english mark:",mark1)
    print("maths mark:",mark2)
    print("science mark:",mark3)
    print("social mark:",mark4)
    print("total is ",total)
    print("average is",average)
    if average > 90:
        print("grade O")
    elif average > 80:
        print("grade A")
    elif average > 70:
        print("grade B")
    elif average > 60:
        print("grade C")
    elif average > 50:
        print("grade D")
    else:
        print("fail")
    print("pass")
else:
    print("english mark:",mark1)
    print("maths mark:",mark2)
    print("science mark:",mark3)
    print("social mark:",mark4)
    print("total is ",total)
    print("fail")