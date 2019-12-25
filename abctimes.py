import re
pattern = '\Zathi'
string = input("enter string= ")
result = re.match(pattern,string)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")