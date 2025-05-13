#decesion making in python
#if statement 

age = 18
if age >= 18:
     print("you are eligible to vote.")
     
#if-else    
age = 16
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

# if-elif-else s statments
marks = 95
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

#nested if 
num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Non-positive number")

#Ternary Operator (Short-hand if-else)
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)
