magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician) #note the indentation, it is important in py to indent the code that belongs to the loop
    print(f"{magician.title()}, that was a great trick!") #you can use f-strings to format the output, and you can use string methods like title() to modify the string before printing it