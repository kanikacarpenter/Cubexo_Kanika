print("Hello,world!") #simple hello world program
a = 5  #integer type
print (type(a))
a = 5.5  #flot type
print (type(a))
a = 2+3j   #complex type
print (type(a))

s = "welcome" #sequence type string data 
print(s)
print(type(s))
print(s[1])
print(s[-2])

a = ["Geeks", "For", "Geeks"] #list type of data in sequence datya types 
print("Accessing element from the list")
print(a[0])
print(a[2])

tup1 = tuple([1, 2, 3, 4, 5])

# access tuple items
print(tup1[0])
print(tup1[-1])
print(tup1[-3])

#string type data ]
a = [1,2,3]
print(a)

b = ["Geeks" , " For" , "Geeks" , 4 , 5]
print(b)
print(type(b))

#tuple dt
tup2 = ('geeks' , 'for')
print("\nTuple with the use of string:" , tup2)
print(type(tup2))

#set data type 
s1 = set()
s1 = set("GeeksForGeeks")
print("set with the use of strings : " , s1)

#list data type imp[lemntation 
fruits = ["apple" , "banana", "orange"]
print(fruits)
fruits.append("grape")
print(fruits)
fruits.remove("orange")
print(fruits)


#variable s
user_name = "kanika"
_hello = 5
marks_12 = 88
print(user_name)
print(_hello)
print(marks_12)
# Define variables with different data types
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

# Get and print the type of each variable
print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))

#scop of the variable 
def f():
    a = "I am local"
    print(a)

f()

#memebership optertor in python
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
