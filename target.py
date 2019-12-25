i = 0
a = {1:10,2:20,3:30,4:40,5:50,6:60}
target = int(input("enter target:"))
for i in range(0,a[i]):
    if (a[i] + a[i + 1] == target):
        print(a[i], a[i + 1])
    else :
        print('enter valid input')