# index warning
name=[]
# print(f"Initial name list: name[0] = {name[0]}")  # This will raise an IndexError because the list is empty
# print(f"last element: name[-1] = {name[-1]}")  # This will also raise an IndexError because the list is empty
# To avoid the IndexError, we can check if the list is not empty before accessing its elements
print(len(name)) # This will print 0 since the list is empty
name.append("alice")
name.insert(0, "bob")  # Insert "bob" at the beginning of the list
print(name)
print(f"First element: name[0] = {name[0]}")  # Now this will work and print "bob"
print(f"Last element: name[-1] = {name[-1]}")  # This will print "alice"