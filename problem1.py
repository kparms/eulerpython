#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9.
#The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000

#Python 2.x

#We can cheat with range(start, stop [,step])

threes = range(3,1000,3)
fives = range(5,1000,5)

#LCM of 3 and 5
fifteen = range(15, 1000, 15)

# [threes] + [fives] - [Three union Fives] 

x = sum(threes)
y = sum(fives)
z = sum(fifteen)

solution = x + y - z
print(solution)
