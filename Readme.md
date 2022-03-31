## Lists

- List is created using Square brackets.
- List is mutable
- Allows Duplicate elements
- Assigning a list to another variable creates reference of the list. Modifying the reference modifies the original.
- To get an actual copy use copy method or use slicing method

<details>

<summary>Python Code</summary>

```python
# Lists : ordered, mutable, allows duplicate elements
mylist = ['bat', 1 , 'cat']
print(mylist)

#Accesing first item(Indexing starts from 0)
firstItem = mylist[0]
print(firstItem)

# Iterating through the list
for item in mylist:
    print(item)

# Check if element present in the list
print('bat' in mylist)
print('dog' in mylist)

#Check number of elemnts in the list using len()
listCount = len(mylist)
print(listCount)

#Insert elements into list
mylist.append('dog')
mylist.insert(1,'Second')
print(mylist)

#Remove element from the list
#remove last elemnt using pop()
pop = mylist.pop()
print(pop)
print(mylist)

#Remove specific element
mylist.remove('Second')
print(mylist)

#Create list using for statement
newList = [2*x for x in range(5)]
print(newList)

#Reverse list 
rev = newList[::-1]
print(rev)

#Copying List
#Reference is copied(Modifying copy modifies original)
mylist = [1,2,3,4]
listRef = mylist

listRef.append(5)
print(mylist)
print(listRef)

#Actual Copying
#Slicing to copy
mylist = [1,2,3,4]
slice_cpy = mylist[:]
slice_cpy.append(5)
print(mylist)
print(slice_cpy)

#Copy method
mylist = [1,2,3,4]
cpy = mylist.copy()
cpy.append(5)
print(mylist)
print(cpy)
```

</details>

## Tuple

- Tuple is ordered and immutable.
- It allows duplicate elements.
- Typically created using parenthesis.
- `tuple()` to create a tuple from list.
- If tuple and a list have same elements then tuple size will be less than size of the list.
- Tuple is much more efficient than list.

<details>

<summary>Python Code</summary>

```python
# Tuple: ordered, immutable, allows dublicate elements
mytuple = ('car','toy','bag')
mytuple1 = tuple([1,2,3,4])

#Slicing a tuple 
slice1 = mytuple[1:3]
print(slice1)

#Create tuple using for loop
mytuple3 = tuple(x*2 for x in mytuple1)
print(mytuple3)
print(type(mytuple3))

#tuple useful methods
print(mytuple.count('car'))
print(mytuple.index('car'))

# tuple to list
mylist = list(mytuple)
print(type(mylist))

#Unpack tuple
x, y, z = mytuple
print(x)
print(y)
print(z)

x, *y, z = mytuple1
print(x)
print(y)
print(z)

#Tuple efficiency
import timeit as tt
print(tt.timeit(stmt="[1,2,3,4,5]",number=1000000))
print(tt.timeit(stmt="(1,2,3,4,5)",number=1000000))
```

</details>

## Dictionaries

- Represented in the form of key-value pair.
- Can be created using curly braces or `dict()`.
- Dictionaries are mutable.
- `dict.keys()` to get keys. `dict.values()` to get values.
- `dict.items()` to get keys and values.
- Use `dict.update()` to update dictionary.
- keys can be strings, numbers or tuples.

<details>

<summary>Python Code</summary>

```python
# Dictionaries: Unordered, key-value pair, Mutable

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

#Copying works in the same way as lists and tuples
cpy = mydict1.copy()
print(cpy)
```

</details>