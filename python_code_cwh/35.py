# Map , Filter and Reduce

#map
def cube(x):
    return x *x *x

print (cube(3))
i = [3,13,4,32,13,45,2,4]

# newl = []
# for item in i:
#     newl.append(cube(item))

newl = list(map(cube,i))
print(newl)

def filter_function(a):
    return a>64
def filter_function2(a):
    return a>4

newnewl = list(filter(filter_function,newl))
newnewl2 = list(filter(filter_function2,i))
print(newnewl)
print(newnewl2)

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] 

# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
  return x + y
  
sum = reduce(mysum, numbers)

# Print the sum
print(sum)