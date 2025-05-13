# Example: Print numbers 1 to 5
for i in range(1, 5):
    print(i)

# Looping through a string
for letter in "Python":
    print(letter)
  

for i in range (1,5):
    print(i)

#while loop 
count = 0
while count < 3:
    print("Hello")
    count += 1

count = 1
while count < 9 :
    print("kanika")
    count += 2

#loop control statments
for i in range(5):
    if i == 3:
        break
    print(i)
    
#numbers
a = 10   #integer
b = 3.14   #float
c = 2+3j    #complex

print(type(a), type(b), type(c))

#strings 
name = "kanika"
print(name[0])
print(name.upper())
print(len(name))

#lists
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits[1])        # banana
print(fruits)           # ['apple', 'banana', 'cherry', 'mango']
fruits.remove("apple")
print(fruits)
print(fruits[2])

#sets
my_set = {1, 2, 3, 2}
my_set.add(4)
print(my_set)           # {1, 2, 3, 4}

#tuple
colors = ("red", "green", "blue")
print(colors[0])        # red


#dictory
student = {
    "name": "Kanika",
    "age": 22,
    "course": "MCA"
}
print(student["name"])       # Kanika
student["age"] = 23
print(student)














"""
tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        print("✅ Task added.")

    elif choice == '2':
        if not tasks:
            print("📭 No tasks found.")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '3':
        if not tasks:
            print("📭 No tasks to delete.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to delete: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"❌ Task '{removed}' deleted.")
            else:
                print("❗ Invalid task number.")

    elif choice == '4':
        print("👋 Exiting To-Do List. Have a nice day!")
        break

    else:
        print("❗ Invalid choice. Please enter 1-4.")

"""
"""

import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)  # update every 1 second

# Create window
root = tk.Tk()
root.title("🕒 Digital Clock")
root.geometry("300x150")
root.configure(bg="black")

# Create label to display time
label = tk.Label(root, font=("Arial", 48), bg="black", fg="lime")
label.pack(expand=True)

update_time()  # Start the clock
root.mainloop()
"""