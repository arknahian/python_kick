# and, or, not

temp = int(input('What is the temperature outside? : '))

if temp >= 0 and temp <= 30 : 
    print('The temperature is good today')
    print('Go outside')

elif temp < 0 or temp > 30 : 
    print('The temperature is bad today')
    print('Stay inside')

else : 
    print('Invalid temperature!')
    

# "not" operator (It basically reverse the condition)

age = int(input('What is your age? : '))

if not(age >=18): 
    print('You still a kid! Lil Bro')

elif not(age < 18): 
    print('you old enough')