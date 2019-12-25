fo=open("newfile.txt","r+")
fo.write("november 24 2019 monday")
str=fo.read(10);
pos=fo.tell();
print ("current position",pos)
position=fo.seek(0,2);
print ("read string is",str)
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
print ("Softspace flag : ", fo.softspace)
fo.close()