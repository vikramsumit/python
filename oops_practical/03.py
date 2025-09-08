class Room:
    def __init__(self, length: float, width: float, height: float):
        if length < 0 or width < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative.")
        self.length = length
        self.width = width
        self.height = height

    def calculate_volume(self) -> float:
        return self.length * self.width * self.height

r = Room(25.5, 14.7, 9.8)
print("Room volume:", r.calculate_volume())  

# Output:
'''raju@kali:~/code only/python/oops_practical % python3 03.py
Room volume: 3673.5299999999997'''
