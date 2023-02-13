# learn base python

name = "python"
name2 = "3.6+"
age = 2

# %-formatting
print("%-formatting")
print("hello in " + name)
print("hello in %s" % name)
print("hello %s in %s" % (name, name2))
print("\n")

# str.format()
print("str.format")
print("hello {} in {}".format(name, name2))
print("hell {1}, you are {0},yes,you are {0} ".format(age, name))

person = {"name": "kobe", "age": "12"}
print("hello,{name},you are {age}".format(name=person["name"], age=person["age"]))

# You can also use ** to do this neat trick with dictionaries:
print("hell,{name},you are {age}".format(**person))

print("\n")

# f-Strings

print("f-strings")
print(f"hello in {name}")
print(f"hello {name.title()} in {name2}")
print(f"hello, my name is {person['name']},and i am {person['age']}")


print("\n")

cars = ["haoda", "toyoto"]
print(len(cars))

# for car in cars:
#     print(car)
#
# print("\n")
#

print("\n")
for temp in range(0, 10, 2):
    print(temp)


print("\n")
square = {x * x for x in range(5)}
for temp in square:
    print(temp)
