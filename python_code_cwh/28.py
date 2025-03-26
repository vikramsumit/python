# FInally CLAUSE


def func():
    try:
        l = [1, 5, 7, 2]
        i = int(input("Enter the index number: "))  
        print(l[i])  
        return 1 
    except IndexError:
        print("Index out of range!")
        return 0  
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return 0
    finally:
        print("I am always executed")  # Always runs


result = func()
print(f"Function returned: {result}")
