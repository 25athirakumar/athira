lastNum = 7
asciiNum = 65
for i in range(0, lastNum):
    for j in range(0, i+1):
        character  = chr(asciiNum)
        print(character, end=' ')
        asciiNum+=1
    print(" ")
