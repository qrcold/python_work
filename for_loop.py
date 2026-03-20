magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician) #note the indentation, it is important in py to indent the code that belongs to the loop
    print(f"{magician.title()}, that was a great trick!") #you can use f-strings to format the output, and you can use string methods like title() to modify the string before printing it
    print(f"I can't wait to see your next trick, {magician.title()}.\n") #you can also add a newline character \n to create a blank line after each magician's message
print("Thank you, everyone. That was a great magic show!") #this line is not indented, so it will be executed after the loop has finished, and it will only be printed once
for i in range(1, 6): #this will loop through the numbers 1 to 5 (the range function generates a sequence of numbers, and the loop will execute once for each number in that sequence)
    print(i) #this will print the current number in the loop, which will be 1, then 2, then 3, then 4, and finally 5