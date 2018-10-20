height = -1 
while height < 0 or height > 23:
    try:
        height = int(input("Height: "))
    except ValueError:
       print("Retry...")
       #height = -1

space = " "
symbol = "#"
count = 1


while height > 0:
    symCount = symbol * count
    spaceCount = space * (height - 1)
    print(spaceCount + symCount + space * 2 + symCount)
    height -= 1
    count += 1
    
    
    
    
    
    
    
    
    
    
    
    


  

    
    



    