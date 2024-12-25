name = 'Bro Code'
first_letter = name[0]
first_name = name[0:3] # or name[:3]
last_name = name[4:8] # or name [4:]

print(first_letter)
print(first_name)
print(last_name)


funky_name = name[0:8:1]
reversed_name = name[::-1]

print(funky_name)
print(reversed_name)

website = 'https://google.com'
sliced = slice(8, -4)
print(website[sliced])