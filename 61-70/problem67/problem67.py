with open("triangle.txt") as f:
    content = f.readlines()
    pos = 0
    row = len(content) -2

    for y in range(0, len(content)):
        content[y] = content[y].split(" ")

    print(content)

    
    while row > 0:
        currow = content[row]
        prevrow = content[row+1]
        print(currow)
        print(prevrow)

        for x in range(0,len(currow)):
            sum1 = int(currow[x]) + int(prevrow[x])
            sum2 = int(currow[x]) + int(prevrow[x+1])

            if (sum1 > sum2):
                currow[x] = sum1
                
            else:
                currow[x] = sum2

        print(currow)
        content[row] = currow
        row -= 1

#    print(len(content))

#    for x in content:        
#        numbers = x.split(" ")
        #Check if pos or pos +1 is greater
#        if (len(numbers) > 1):
#            if (numbers[pos] > numbers[pos+1]):
#                print (numbers[pos])
#                sum += int(numbers[pos])
#            else:
#                pos += 1
#                print (numbers[pos])
#                sum += int(numbers[pos])

#print (sum)
