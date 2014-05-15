#Lattice Paths
#Find the number of paths in a 20x20 grid
#Sarah has figured that this is based off Pascals triangle
#Using combinations we are able to calculate the number of paths in a 
#20x20 grid, the base of this is factorial

def factorial(number):
    total = 1
    while number > 1:
        total = total * number
        number-=1
    return total
        
print (factorial(40)/(factorial(20)*factorial(20)))
