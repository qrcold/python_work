list =['phil','smiley','paul','zack']
print(f"{list[0].title()},hello")
print(f"{list[1].title()},hello")
print(f"{list[2].title()},hello")
cannot_come=list[3]
list.remove('zack')
print(f"{cannot_come.title()},can not come")
print("I found a larger table.")
list.insert(1,'zib')
print(list)
list.insert(2,'Dave')
print(list)
list.append('hack')
print(list)
print(f"{list.pop()},sorry")
print(f"{list.pop(2)},sorry")
print(f"{list.pop()},sorry")
print(f"{list.pop()},sorry")
print(list)
print(f"{list[0].title()},you are still in the list.")
print(f"{list[1].title()},you are still in the list.")
del list[0]
del list[0]
print(list)