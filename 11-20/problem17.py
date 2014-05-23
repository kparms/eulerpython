ones = {
    0:"",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen"
}

tens = {
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety"
    }


def getNumberText(num):
    #print(num)
    result = ""
    if (num < 20):
        result = ones[num]

    if (num > 19 and num < 100):
        numstring = str(num)
        tendigit = numstring[0] + "0"
        #print(tendigit)
        result = tens[int(tendigit)]
        #print(tens[int(tendigit)])
        num -= int(tendigit)
        #print(ones[num])
        result += " " + ones[num]
        #print (result)

    if (num > 99 and num < 1000):
        numstring = str(num)
        hundreddigit = numstring[0]
        result = ones[int(hundreddigit)] + " hundred"
        hundreddigit += "00"
        num -= int(hundreddigit)

        #We don't need the 'and' if 100, 200, 300, etc.
        if (num > 0):
            result += " and "

        if (num < 20):
            result += ones[num]
        else:
            tendigit = numstring[1] + "0"
            #print(tendigit)
            result += tens[int(tendigit)]
            #print(tens[int(tendigit)])
            num -= int(tendigit)
            #print(ones[num])
            result += " " + ones[num]
    return result

    
def getNumTextLen(strnum):
    strnum = strnum.replace(" ","")
    #print (strnum)
    return len(strnum)

total = 11 #This is the length of "One Thousand"
for x in range(1,1000):
    #print (x)
    total += getNumTextLen(getNumberText(x))
    #print(total)

print (total)

#print(getNumTextLen(getNumberText(115)))
