with open("input.txt") as f:
    content = f.readlines()
    sum = 0
    for x in content:
        sum += int(x.strip())

    print (sum)
