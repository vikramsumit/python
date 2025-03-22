dict = {
    "sumit": "completed matrcinesoi isdjfoi",
    "class" : "currently at house",
    "status": "unemployed"
}
# ,{"sumit": "completed matrcinesoi isdjfoi",
#     "class" : "currently at house",
#     "status": "unemployed"}
print(dict)
print(dict.keys())
print(dict.values())
# print(dict["status"])

for key in dict.keys():
    print(f"the value correspondint to the key {key} is {dict[key]}")
