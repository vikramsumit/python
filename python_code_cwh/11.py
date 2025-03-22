# i = int(input("enter the number:"))
for i in range(12):
    print("5 X ", i+1 , "=", 5 * (i+1))
    if(i == 10):
        break
    
print("loop khatm hogya table ka")


for i in range(12):
    if(i == 5):
        print("iteration skipped")
        continue
    print("5 X ", i , "=", 5 * i)
    