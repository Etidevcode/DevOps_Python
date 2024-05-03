planet1 = "Closest of Sun"
print(planet1)

print(planet1[0])
print(planet1[1])
print(planet1[2])

print("***"*5)
print(planet1[-1])
print(planet1[-2])
print(planet1[-3])
print("***"*5)

# Slicing a string, get a substring from a string
print(planet1[1:4])
print(planet1[:])
print(planet1[:7])
print(planet1[:11])
print("***"*5)

devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")
print(devops[0])
print(devops[4])
print(devops[-1])

print(devops[2:5])
print(devops[2:5][0])

print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-1])
print("***"*15)
# Slicing List
devops = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]
print(devops[0])
print(devops[4])
print(devops[-1])

print(devops[2:5])
print(devops[2:5][0])

print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-1])
print("***"*15)

# Dictionary Example
skills = {
    "devOps": ("AWS", "Jenkins", "Python", "Ansible"),
    "Development": ["Java", "NodeJS", ".net"]
}

print(skills)
print(skills["devOps"])
print(skills["Development"])

print(skills["devOps"][-1])
print(skills["devOps"][-1][:3])