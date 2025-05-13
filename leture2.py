age = 16

if(age >= 18):
    print("can vote & apply for license")
else:
    print("you con't vote and apply")

    light = "blue"
    if(light == "red"):
        print("stop") #indentation
    elif(light =="green"):
        print("go")
    elif(light == "yellow"):
        print("look")
    else:
        print("light is broken")

    print("end of code")
    #grade system 

    marks = 80 
    if(marks>= 90):
        grade = "A"
    elif(marks >=80 and marks<90):
        grade = "B"
    elif(marks >= 70 and marks<80):
        grade = "C"
    else:
        garde = "D"

    print("grade of the student -> ", grade)

    #nesting

    age = 95

    if(age >= 18):
        if(age >= 80):
            print("cannot drive")
        else:
            print("can drive")
    else:
        print("cannot drive")

num = int(input("Enter number: "))

if num % 2 == 0:
    print("EVEN")
else:
    print("ODD")

#LARGEST NUMBER FIND OUT CODE
a = int(input("enter first number: "))
b = int(input("enter second number :"))
c = int(input("enter third number:"))
if(a >= b and a >=c):
    print("first number is largest ", a)
elif(b >=c ):
    print("second number is latgest",b)
else:
    print("third is largest" , c)

#7 multiple number%
x = int(input("Enter number: "))

if(x%7== 0):
    print("multiple of 7")
else:
    print("not a multiple")

    x = int(input("Enter a number: "))

match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid number")
