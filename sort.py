# homework1: sorting a list in different ways
# Create a list of at least five items (strings).
destinations = ['paris', 'tokyo', 'new york', 'sydney', 'rome']
# Print the list in its original order. Don't worry about the neatness of the output; just print the original Python list.
print("Original list:")
print(destinations)
# Use sorted() to print this list in alphabetical order, without modifying it.
print("Sorted list (alphabetical):")
print(sorted(destinations))
# Print the list again to verify that the order remains unchanged.
print("Original list (unchanged):")
print(destinations)
# Use sorted() to print this list in reverse alphabetical order, without modifying it.
print("Sorted list (reverse alphabetical):")
print(sorted(destinations, reverse=True))
# Print the list again to verify that the order remains unchanged.
print("Original list (unchanged):")
print(destinations)
# Use reverse() to modify the order of the list elements. Print the list to verify that the order has indeed changed.
destinations.reverse()
print("List after reverse():")
print(destinations)
# Use reverse() again to modify the order of the list elements. Print the list to verify that it has returned to the original order.
destinations.reverse()
print("List after reverse() again (original order):")
print(destinations)
# Use sort() to modify the list so that its elements are arranged in alphabetical order. 
# Print the list to verify that the order has indeed changed.
destinations.sort()
print("List after sort() (alphabetical order):")
print(destinations)
# Use sort() to modify the list so that its elements are arranged in reverse alphabetical order. Print the list to verify that the order has indeed changed.
destinations.sort(reverse=True)
print("List after sort() (reverse alphabetical order):")
print(destinations)
# remember: in py,variables are not nesessarily initiallized
# and remenber sets are unordered collections of unique elements
# here is an example of sorting a set
# name.sort()
# print(name)
# name.sort(reverse=True)
# print(name)

