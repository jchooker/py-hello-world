# print("Hello World")

# name = "Joseph Hooker"
# print("My name is " + name)
# print("My name is", name)

num = 26
print("Hello,", num, "!")
print("Hello, " + str(num) + "!") #resolved issue with concatenation

food1 = "tuna mac"
food2 = "veggie pizza"
actual_age = 36
print("I love to eat {} and {}, despite being {}".format(food1, food2, actual_age)) #4a

print(f"I love to eat {food1} and {food2}, despite being {actual_age} years of age.") #4b

str1 = "an example of a string to do various operations with" #last bonus section

print(str1.split())

prep1 = str1.count("of")
prep2 = str1.count("with")

print(f"There are {prep1+prep2} prepositions in this string")
