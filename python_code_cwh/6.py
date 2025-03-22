# some basics functions
# Strings are immutable
a = "rajubhai !!!!!! rajubhai !!!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("rajubhai", "babubhai"))
print(a.split(" "))

channel = "hello guys LSKJEI Welcome back herE"
print(channel.capitalize())

str1 = "Jungle mein aap sabhi ka swagat hai"
print(len(str1))
print(len(str1.center(55)))
print(len(str1))
print(a.count("rajubhai"))

str1 = "is ur name raju????"
print(str1.endswith("?"))

str1 = "is ur name raju????"
print(str1.endswith("name", 3, 10))

str1 = "is ur name raju????"
print(str1.endswith("name", 3, 8))
print(str1.find("ur"))
print(str1.find("urkh"))
print(str1.index("ur"))
# print(str1.index("urooo"))

srt2 = "welcomeeveryonehere"
print(srt2.isalnum())
print(srt2.islower())
print(srt2.isalpha())

str1 = "We wish you a MerryChristmas\n"
print(str1.isprintable())
str1 = "         "  # using Spacebar

print(str1.isspace())
str2 = "            "  # using Tab
print(str2.isspace())

str1 = "World Health Organization "
print(str1. istitle())

str2 = "To kill a Mocking bird"
print(str2. istitle())

str1 = "Python is an Interpreted Language"
print(str1. startswith("Python"))

str1 = "Python is an Interpreted Language"
print(str1. swapcase())

str1 = "He's name is Dan. Dan is an honest man. "
print(str1.title())
