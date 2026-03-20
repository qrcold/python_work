# use ctrl + / to comment out a block of code in pycharm, and ctrl + shift + / to uncomment it
# magicians = ['alice', 'david', 'carolina'] 
# for magician in magicians: 
#     print(magician) #note the indentation, it is important in py to indent the code that belongs to the loop
#     print(f"{magician.title()}, that was a great trick!") #you can use f-strings to format the output, and you can use string methods like title() to modify the string before printing it
#     print(f"I can't wait to see your next trick, {magician.title()}.\n") #you can also add a newline character \n to create a blank line after each magician's message
# print("Thank you, everyone. That was a great magic show!") #this line is not indented, so it will be executed after the loop has finished, and it will only be printed once
for i in range(1, 6): #this will loop through the numbers 1 to 5!!!!!        
    # (the range function generates a sequence of numbers, and the loop will execute once for each number in that sequence)
    print(i) #this will print the current number in the loop, which will be 1, then 2, then 3, then 4, and finally 5
numbers=list(range(1,20))
print(numbers) 
evennums=list(range(2,21,2)) #this will generate a list of even numbers from 2 to 20 (the third argument in the range function specifies the step size, so it will skip every other number)
print(evennums)

# below is an example of ** to calculate the square of a number(value**x(in py.)==pow(value,x)in c.)

squares=[] #this will create an empty list to store the squares of the numbers
for value in range(1,11):
    square=value**2 
    squares.append(square) 
print(squares)

# you can also use a list comprehension to create the list of squares in a more concise way
squares=[value**2 for value in range(1,11)]
print(squares)


# below are some functions(max,min,sum)
digits=[1,2,3,4,5,6,7,8,9]
print(min(digits)) 
print(max(digits)) 
print(sum(digits)) 

#exercise: use a for loop to generate a list of the first 10 cubes (the cube of a number is that number raised to the third power)
cubes=[value**3 for value in range(1,11)]
print(cubes)

