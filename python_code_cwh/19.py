# info = "hey my name is {1} and i am from {0}"
# name = "raju"
# country = "india"

# print(info.format(name,country))
# print(info.format(country,name))

name = "babu"
planet = "mars"
print(f"hey my name is {name} and i am from {planet}")
print(f"when we want to show as it is means (no change)hey my name is {{name}} and i am from {{planet}}")
print(f"when we want to show as it is means (\033[1mno change\033[0m) hey my name is {{name}} and i am from {{planet}}")
# 033[1m starts the bold formatting.
# 033[0m resets it back to normal.

price = 4.564658
txt = f"For only {price:.2f} rupee!"
print(txt)

print(type(f"{25*57}"))