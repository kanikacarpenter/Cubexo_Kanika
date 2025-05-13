"""
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.append("kanika")
print(thislist)
thislist.remove("kanika")
print(thislist)

print(thislist[-1]) #access throghout the index

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
"""
"""
#global variable
x = "awesome"
print ("python is "+ x)
#myfun()

#assign multiple values 
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#add multiple output
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)"""

#expection handling 
a = input("enter the number : ")
print(f"Multiplication table of {a} is : "
)
try:
    for i in range(1,11):
      print(f"{int(a)} * {i} = {int(a)*i}")
except:
    print("Invalid Input!")

print("Some imp lines of code")
print("End of program ")