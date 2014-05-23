with open("triangle.txt") as f:
    content = f.readlines()
    sum = 75
    pos = 0
    for x in content:        
        numbers = x.split(" ")
        #Check if pos or pos +1 is greater
        if (len(numbers) > 1):
            if (numbers[pos] > numbers[pos+1]):
                print (numbers[pos])
                sum += int(numbers[pos])
            else:
                pos += 1
                print (numbers[pos])
                sum += int(numbers[pos])

print (sum)
