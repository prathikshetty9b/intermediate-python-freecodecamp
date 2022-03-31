# Dictionaries: Unordered, key-value pair, Mutable
from multiprocessing.sharedctypes import Value


mydict = {"name":"max","age":28}
print(mydict)

mydict1 = dict(name="Ram", age = 27)
print(mydict1)

# Add new key-value
mydict1['email'] = 'ram@xyz'
print(mydict1)

#deleting a key
del mydict1['email']
print(mydict1)

#Pop an element
print(mydict.pop('age'))
print(mydict)

#looping in dictionary
for key in mydict1:
    print(key)

for key in mydict1.keys():
    print(key)

for values in mydict1.values():
    print(values)

for key,value in mydict1.items():
    print(key,value)

