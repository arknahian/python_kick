name = 'foggo mcLovin'
numeric_name = '1232'
name_with_nospace = 'foggomcLovin'

print(len(name)) #space counts
print(name.find('L')) #however with "l" output will be -1
print(name.capitalize()) # //Foggo mclovin
print(name.upper()) # //FOGGO MCLOVIN
print(name.lower()) # //foggo mclovin

print(name.isdigit()) # false
print(numeric_name.isdigit()) # true

print(name.isalpha()) # False (Because of the space)
print(name_with_nospace.isalpha) # True

print(name.count('o')) # 3

print(name.replace('o', 'a')) # fagga mcLavin

print(name * 3)
