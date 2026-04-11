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
cubes=[pow(value, 3) for value in range(1,11)]
print(cubes)
#actually, in python, you can still use pow() like C or other languages.

#below are patial list slicing
players=['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #this will print the first three players in the list (the 0:3 stops before 3 ,so it will print the elements at indices 0, 1, and 2)

#0:3 is similar to MATLAB's 1:3, but in python, the index starts at 0, so the first element is at index 0, the second element is at index 1, and so on. Therefore, the slice 0:3 will include the elements at indices 0, 1, and 2, which are 'charles', 'martina', and 'michael'.
# :3 is also similar to 1:3 in MATLAB, but it will include all the elements from the beginning of the list up to (but not including) index 3. 
#3: is similar to 4:end in MATLAB, but it will include all the elements from index 3 to the end of the list. 
#negative such as -3: will include all the elements from the third-to-last element to the end of the list. (Note that the direction is still from left to right)
print(players[-3:])

#below are some examples of copying a list
my_foods=['pizza', 'falafel', 'carrot cake']
friend_foods=my_foods[:] 
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)