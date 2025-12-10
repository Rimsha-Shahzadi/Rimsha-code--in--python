# table = int(input("Enter a number to print a table: "))
# for i in range(1,11):
#     print(f"{table}*{1} = {table*i}")

# print("Rimsha","Jannat", "Ismail")
# n = 10
# for i in range(11):
#   print(i)

# message: str = "PIAIC student card\n Father's name"
# print(message)
# name: str = "Rimsha Shahzadi"
# fname: str = "Muhammad Arif"
# education: str = "Graduation"
# age : int = 24

# card : str = "PIAIC Student Card\nStudent Name:" + name +\
# "\nAge:" + str(age) +"\n"+\
# "Education: " + educaton

# print(card)

# print(1+8+9)
# print(1+ \
#       8+ \
#         3)

# Multiline string
# card : str = """
# PIAIC Student Card
# Student Name: Rimsha Shahzadi
# Age: 24
# Education: Graduation

# """
# print(card)

#F-STRING Python
# name: str = "Rimsha Shahzadi"
# fname: str = "Muhammad Arif"
# education: str = "Graduation"
# age : int = 24

# card : str = f"""
# PIAIC Student Card
# Student Name: {name}
# Father's Name:  {fname}
# Age: {age}
# Education: {education}

# """
# print(card)
 #Jinja style
# name: str = "Rimsha Shahzadi"
# """
# Student Name {{name}}
# """
# print(name)

# [i for i in dir(str) if "__" not in i]
# name: str = "Rimsha Shahzadi"
# fname: str = "Muhammad Arif"
# education: str = "Graduation"
# age : int = 24
# card : str = """
# PIAIC Student Card
# Student Name: {0}
# Father's Name:  {1}
# Age: {3}
# Education: {2}
# """.format(name, fname, education, age)
# print(card)
# name : str = "Rimsha Shahzadi"
# print(name.capitalize())
# print(name.lower())

# a = 5
# b = 10
# print("pakistan valuea ={} and value b ={}".format(a,b))
# Student_code: str = """
# print("My Name is Rimsha")
# a : int = 12
# b : int = 12
# print(a+b)
# """
# exec(Student_code)

#Pre define global functions we have used
#print
#type
#id
#dir
#len

# a : list[str] = [i for i in dir(str) if "__" not in i]
# print(a)
# print(len(a))
# name : str = "     Rimsha Shahzadi     "
# print(name)
# print(name.lstrip())
# print(name.rstrip())

# import re
# name : str = "   Rimsha     Shahzadi    "
# print(name)
# name1 : str = re.sub(' {2,100}', ' ', name).strip()
# print(name1)

# name : str = "Rimsha Shahzadi"
# print(name)
# print(name.title())

# name : str = "I Love Python"
# print(name)
# print(name.upper())
# print(name.lower())

print("Name:\t\tRimsha Shahzadi")
print("Name:\nRimsha Shahzadi")
print("Name:\bRimsha Shahzadi")