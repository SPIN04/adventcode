with open("2024/1/input.txt", "r") as file:
    col1,col2=[],[]
    sum=0
    for line in file:
        col1.append(line.split("   ")[0])
        col2.append(line.split("   ")[1].replace("\n",""))
    col1.sort()
    col2.sort()
    
    
    for i,num in enumerate(col1):
        nums=[]
        nums.append(num)
        nums.append(col2[i])
        nums.sort()
        sum+=int(nums[1])-int(nums[0])
        
    print()
    print(sum)
