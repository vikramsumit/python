# with open('myfile.txt','r') as f:
#     print(type(f))
#     f.seek(10)
#     print(f.tell())
#     data = f.read(11)
#     print(data)
#     f.close()

with open('sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(5)

with open('sample.txt', 'r') as f:
#   print(f.read())