for i in range(10):
    if i == 15:
        break
    print(i, end=' ')

for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end = ' ')

for i in range(5):
    if i == 2:
        pass  # Placeholder, no action taken
    print(i)
