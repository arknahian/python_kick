#kick off
name = 'Ark'
age = 21
isStudent = True

print(name)
print(age)
print(isStudent)



# string operation
first_name = 'John'
last_name = 'Due'
print("Hello " + first_name + " " + last_name)
print(type(first_name)) # str



# integer operation
salary = 1200

salary += 1 #short for (salary = 1200 + 1)

print(salary)
print(type(salary)) # int



# string + integer operation
# print(first_name + " " + salary) [This won't work!]
print(first_name + str(salary)) # gotta convert it to string


#float type operation 
height = 250.5
print(type(height)) # float
print('Your height is: ' + str(height)) # notice it's converted to str()



#Boolean data type
human = False
print(type(human)) # bool
print("Are you a human: " + str(human))



# multiple assignment 
name, age, attractive = 'Mark', 28, False

print(name) # It updated the last assigned value : Mark not "Ark"
print(age)
print(attractive)

# spongebob = 30
# patrick = 30          (we can write this in one line of code)
# sandy = 30

spongebob = patrick = sandy = 30

print(spongebob)
print(patrick)
print(sandy)

