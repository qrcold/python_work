name="\t\n  Eric  \t\n"
# initiate a variable
# print(name)
# bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
# message = f"My first bicycle was a {bicycles[0].title()}." 
# print(message) 
# donot forget the ()
#  before remove ,there should be space for claiming the list 
# insert (index,value)
# press ctrl+B to run the program
names=['abandon','back','can','do']
print(f"hello, {names[0].title()}")
names[1] = 'qrcolds'
names.insert(1,'open')
print(names[1])
fun=names[2]
del names[2]
print(f"{fun},hello")
names.remove('do')
print(names[2])

names.append('dhiaol')

print(names)
motorcycles = ['honda', 'yamaha', 'suzuki']  
last_owned = motorcycles.pop(1) 
print(f"The last motorcycle I owned was a {last_owned.title()}.") 
