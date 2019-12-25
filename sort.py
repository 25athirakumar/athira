def bubble_sort(list):
   for i in range(len(list)-1,0,-1):
	  for j in range(i):
         print (list[j],list[j+1])
         if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
list=[9,8,7,5,1,11]
bubble_sort(list)
print(" The sorted list is : ",list)
