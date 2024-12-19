with open("2024/1/input.txt", "r") as file:
    col1,col2,tosum=[],[],[]
    for line in file:
        col1.append(int(line.split("   ")[0]))
        col2.append(int(line.split("   ")[1].replace("\n","")))
    col1.sort()
    col2.sort()
    
    
    for i,num in enumerate(col1):
        
        ripetizioni=col2.count(num)
        tosum.append(ripetizioni*num)
    print()
    print (sum(tosum))