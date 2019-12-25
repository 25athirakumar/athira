name={1:'a',2:'b',3:'c',4:'d',5:'e'}
dob={1:20,2:30,3:10,4:50,5:60}
amount=500
n=input("enter name: ")
d=int(input("enter your dob: "))

for i in range (1,6):
    if n==name[i]:
        if d==dob[i]:
            k=int(input("enter deposit[1] or debit[2] or both[3]= "))
            if k==1:
                deposit=int(input("enter amount to deposit: "))
                amount=amount+deposit
                print("total amount in account: ",amount)
            elif k==2:
                deb=int(input("enter amount to debit: "))
                amount=amount-deb
                if(amount<=500):
                    print("minimum amount to be in account is 500")
                else:
                    print("total amount  ",amount)
            elif k==3:
                deposit=int(input("enter amount to deposit: "))
                deb=int(input("enter amount to debit: "))
                amount=((amount+deposit)-deb)
                if(amount<=500):
                    print("minimum amount to be in account is 500")
                else:
                    print("total amount  ",amount)
            else:
                print("enter valid k")
        else:
            print("invalid")
            break;