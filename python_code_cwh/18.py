countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

Tuple1 = (0, 1, 2, 2,34,32,3, 2,3,543,234,4,3,3,3,3 ,3, 1, 3, 2)
print(len(Tuple1))
res = Tuple1.count(3)
res2 = Tuple1.index(3,0,19)
print('Count of 3 in Tuple1 is:', res)
print('Count of 3 in Tuple1 is:', res2)

Tuple = (0, 1, 2, 2,34,32,4,3, 2,3,543,234,4,3,3,3,3 ,3, 1, 3, 2)
print("Length of tuuple:",len(Tuple))
countof3 = Tuple[1:15].count(3)

# res = Tuple.index(3)
res = Tuple.index(3,2,9)
res2 = Tuple.index(3,2,18)
print('First occurrence of 3 is', res)
print('First occurrence of 3 is', res2)
print("Number of occurence of 3 between index 1 and 15:", countof3)

tuple_data = (0, 1,3,3, 2, 2, 34, 32, 4, 3, 2, 3, 543, 234, 4, 3, 3, 3, 3, 3, 1, 3, 2)
print(len(tuple_data))
sliced_tuple = tuple_data[4:23]
sliced_tuple2 = tuple_data[2:9]
print(sliced_tuple)
print(sliced_tuple2)
Icount_of_3 = sliced_tuple.count(3)
IIcount_of_3 = sliced_tuple2.count(3)

print("Number of occurrences of 3 between indices 4 and 19:", Icount_of_3)
print("Number of occurrences of 3 between indices 4 and 19:", IIcount_of_3)
