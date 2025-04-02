with open('myfile.txt','r') as f:
    print(type(f))
    f.seek(10)
    print(f.tell())
    data = f.read(11)
    print(data)
    f.close()