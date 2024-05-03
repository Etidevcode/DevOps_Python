# String Build in Methods/Functions
message = "corona vaccine is ready to use, 90% effective."
print(message)
print(message.capitalize())
print("===="*20)
Message = message.capitalize()
print(Message)
print("===="*20)

# dir() function
"""
print("===="*20)
print(dir(""))
print("===="*20)
print(dir([]))
print("===="*20)
print(dir(()))
print("===="*20)
print(dir({}))
print("===="*20)
"""
"""
print(message.upper())
print("===="*20)
print(message.islower())
print(message.isupper())

"""

"""
print(message.find("ready"))
print(message[18:24])
print(message.find("not"))
"""

"""
seq = ("192", "168", "40", "90")
print(".".join(seq))
print("/".join(seq))
print("-".join(seq))
"""

"""
mountains = ["Everest", "Himalaya", "Sahyadri", "Alps", "K2", "Mt Hood"]
print(mountains)
print("===="*20)

mountains.append("Oregon mount")
print(mountains)
print("===="*20)

mountains.extend(["Mt Rainer", "Satpuda"])
print(mountains)
print("===="*20)

mountains.insert(2, "Tropicana")
print(mountains)
print("===="*20)

mountains.pop()
mountains.pop()
mountains.pop()
print(mountains)
mountains.pop(5)
print(mountains)
"""

cntr_emp1 = {
    "Name": "Santa",
    "Skill": "Blockchain",
    "Code": 1024
}

print(cntr_emp1.keys())
print(cntr_emp1.values())
print(cntr_emp1.clear())
print(cntr_emp1)