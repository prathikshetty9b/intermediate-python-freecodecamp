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

