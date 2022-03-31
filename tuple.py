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