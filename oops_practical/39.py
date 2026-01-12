# Take a user-defined array and display it. Do exception handling, if array index out ofbound otherwise execute code when there is no error.


try:
    arr = [81, 22, 3, 4, 5,32,53,234,5,23,433,43,0]
    print("Array:", arr)
    
    index = 8
    print(f"Element at index {index}: {arr[index]}")
except IndexError:
    print(f"Error: Index {index} is out of bounds for array of length {len(arr)}.")
else:
    print("No error occurred. Code executed successfully.")