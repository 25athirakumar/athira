x = int(input("\nenter the number "))
def armstrong(x):
           Sum = 0
           Times = 0
           Temp = x
           while Temp > 0:
                      Times = Times + 1
                      Temp = Temp // 10
           Temp = x
           for n in range(1, Temp + 1):
                      Reminder = Temp % 10
                      Sum = Sum + (Reminder ** Times)
                      Temp //= 10
           return Sum
if (x == armstrong(x)):
    print("\n %d is Armstrong Number.\n" %x)
else:
    print("\n %d is Not a Armstrong Number.\n" %x)