# String's
str1 = "alpha"
str2 = 'beta'
str3 = '''gamma string'''
str4 = """delta string"""

# Numbers
num1 = 123
flt1 = 2.0

# List : Collection of multi datatype, enclose in square brackets.
first_list = [str1, "DevOps", 47, num1, 1.2]

# printing a list
print(first_list)

# Tuple / Collection of multi datatype, enclosed in round bracket
first_tuple = (str1, "DevOps", 47, num1, 1.5)
print(first_tuple)

# Dictionary / Elements in the dictionary are always in pairs(Key:Values), curly brackets.
first_dictionary = {
    "Name": "Etienne",
    "Weight": 76,
    "Exercises" : ["Boxing", "Dancing", "Jogging"]
}

# Printing a Dictionary
print(first_dictionary)

print("Variable first_list is a : ", type(first_list))
print("Variable first_list is a : ", type(first_tuple))
print("Variable first_list is a : ", type(first_dictionary))

# Boolean
x = True
y = False

# Printing Boolean
print("x is a : ", type(x))
print("y is a : ", type(y))