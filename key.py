#oops class
class Dog :
    sound = "bark"

#create an object from the class
dog1 = Dog()    

#Access the class attribuire 
print(dog1.sound)

#oops object
"""
courses = ['history' , 'math', 'physics', 'computer']

nums = [1,5,2,4,3]

courses.sort()
nums.sort(reverse=True)

sorted_courses = sorted(courses)

courses.reverse()
print(courses)
print(nums)
print(max(nums))
print(min(nums))
"""

#list examples
courses = ['History' ,'Math','Physics','Computer']

for course in courses:
    print(course)

course_str = ' - '.join(courses)

print(course_str)

try : 
    x = 3/0
    print(x)
except:
    print("An exception occurred . ")




