tup = (1, 3,5,56,64,"blue", False)
print(tup)
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[6])
print(tup[-4])
print(tup[-6])
# print(tup[1876])

if 64 in tup:
    print("yes 64 ks present in tupoe")
    
tup2 = tup[:5]
print(tup2)