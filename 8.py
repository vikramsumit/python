# find
s = "hello trhis id is of world"
print(s.find("world"))  # Output: 6

#count words
s = "hello world hello"
print(s.count("hello"))  # Output: 2

# letter
s = "hello"
print(s.upper())  # Output: "HELLO"

s = "HELLO"
print(s.lower())  # Output: "hello"

s = "hello"
print(s.capitalize())  # Output: "Hello"


# Cptilizes first word
s = "hello world"
print(s.title())  # Output: "Hello World"

# remove unwanted spaces
s = "  hello  "
print(s.strip())  # Output: "hello"

# replace
s = "hello world"
print(s.replace("world", "Python"))  # Output: "hello Python"

# split
s = "hello world"
print(s.split(" "))  # Output: ["hello", "world"]

# join 
words = ["hello", "world"]
print(" ".join(words))  # Output: "hello world"

