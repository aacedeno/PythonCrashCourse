#Use a for loop to print the numbers from 1 to 20, inclusive.

for i in range(21):
    print(i)

#Make a list of the numbers from one to one million, and then use a for loop to print the numbers.

for i in range (1_000_000):
    print(i)

#Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
million = [range (1_000_000)]
for i in million:
    print(max(i))
    print(min(i))
    print(sum(i))

# #Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number
for i in range(1, 21, 2):
    print(i)

# #Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list
for i in range(3,31,3):
    print(i)

#A number raised to the third power is called a cube. For example the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
#is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

for i in range (1,11):
    print(i**3)

#Use a list comprehension to generate a list of the first 10 cubes.
cube = [i**3 for i in range(1,11)]
print(cube)