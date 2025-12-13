# import pandas as pd
# table = pd.read_html("https://www.w3schools.com/python/python_operators.asp")
# print(table)
# print(table[0])
  
# import pandas as pd
# df = pd.read_html("https://www.w3schools.com/python/python_operators.asp")
# print(len(df), "tables found")
# print(df[0])

# a : int  = 7
# b : int  = 2
# print(a + b)    # Addition
# print(a - b)    # Subtraction
# print(a * b)    # Multiplication
# print(a / b)    # Division
# print(a % b)    # Modulus
# print(2**3)
# print(200 // 2)


# assignment operator
# r : int = 5
# s : int = 8
# print(r)
# r +=5
# print(r)

# r : int = 5
# s : int = 8
# print(r)
# r -=5
# print(r)

# r : int = 5
# s : int = 8
# print(r)
# r *=5
# print(r)

# r : int = 5
# s : int = 8
# print(r)
# r /=5
# print(r)

# r : int = 5
# s : int = 8
# print(r)
# r %=5
# print(r)

# r : int = 5
# s : int = 8
# print(r)
# r //=5
# print(r)

# r : int = 5
# s : int = 8
# print(r)
# r **=5
# print(r)

# comparison operator

# w : int = 4
# x : int = 8
# print(w == x)

# w : int = 4
# x : int = 4
# print(w == x)

# w : int = 4
# x : int = 8
# print(w != x)

# w : int = 4
# x : int = 8
# print(w > x)

# w : int = 4
# x : int = 8
# print(w < x)

# w : int = 4
# x : int = 8
# print(w >= x)

# w : int = 4
# x : int = 4
# print(w <= x)

# ascii code
# Z = 90

# a = 97
# z = 122
# 0=48
# 9=57
# ord('A')
# chr(65)

# a : str = 'A'
# b : str = 'B'
# print(b >= a)

# logical operators

# print(True and True and True and True)
# print(True and True and False and True)
# print(False and False and False and True)

# print(True or True or True or True)
# print(True or True or False or True)
# print(False or False or False or True)
# print(True)
# print(not True)

# name: str = "Rimsha"
# print(not name =="Rimsha") 


# identity operators
# x : str = 'abc'
# y: str = 'abc'
# print(id(x))
# print(id(y))
# print(x is not y)
# names : list[str] = [chr(i) for i in range(65, 91)]
# print(names)
# print("Pakistan" in names)

# names : list[str] = ["Rimsha", "Ismail", "Jannat"]
# uinput: str =input("Enter your name: ")
# print(uinput  not in names)

# print(3+2-4*5/5+3)
# a,b,c ="Rimsha", 2.4, 6
# print(a)
# print(b)
# print(c)

# data = ("Rimsha", 4, 3.0)
# print(*data)

# print("Rimsha" *5)
a : int = 50
if (a < (b := a+20)):
    print(b)
else:
    print("else is working") 