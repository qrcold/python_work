# learn how to sort a list
# remember: in py,variables are not nesessarily initiallized
# and remenber sets are unordered collections of unique elements
# here is an example of sorting a set
name=['apple','candy','banana','pie']
# name.sort()
# print(name)
# name.sort(reverse=True)
# print(name)
print("Here is the sorted list:\n")
print(sorted(name))
# print("Here is the original list:")
# print(name)
temp=name
name.reverse()
print("Here is another reversed list:")
print(name)
temp.sort(reverse=True)
print("Here is another sorted list in descending order:")
print(temp)
print("actually there's difference between .reverse() and reverse=True")
print("because .reverse() changes the order of the original list")
print("while reverse=True just displays the list in descending order")
print("so the original list is now changed to:")
print(name)
print("notice that temp is just a reference to name")
# to run this code, save it in a file named 'sort.py'
# then in 'terminal' input 'python sort.py' to run the code
# and then you will see the sorted list printed out
# press"up" arrow to see the previous commands
# press"ctrl+c" to exit the terminal