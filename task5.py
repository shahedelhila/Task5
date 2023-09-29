
# 1
print('Enter your (name , age , street , city , country)\n')
Name = 'lama'
Age = 20
street = '159'
city = 'Gaza'
country = 'Palestine'
# 2
print(f'     "Name:{Name}"\n'
      f'       "Age:{Age}"\n'
      f'"Address:{street},{city},{country}"\n')
# 3
print('"Hello {Lama} Your age is 15 Years Old, Your\n Address is 159, Gaza, Palestine."\n')
# 4
print(type(Name), type(Age))
print(type(street), type(city))
print(type(country), '\n')
# 5
print('"Hello Lama, How Are You? \ """ Your Age Is "15"" + \n'
      'And Your Country Is: Palestine\n')
# 6
print('"Hello Lama, How Are You? \ \n""" Your Age Is "15"" + '
      'And\n Your Your City Is: Gaza \n')

# 7
name = 'ITF Gsg Python'
print('First Letter Is "', name[0], '"')
print('Third Letter Is "', name[2], '"')
print('Last Letter Is "', name[-1], '"')

# 8
print(name[11:15])
print(name[0:3])
print(name[0:7:2])
print(name[-1:-7:-1])

# 9
name1 = "$&$&Mohammed$&$&"
print(name1.strip('$&$&'))

# 10
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7","love"))

# 11 12
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num6)

# 13
# In title each letter is adapted at the beginning of the words in the sentence.
# Only capitalize will zoom in on the first letter in the sentence.
# title>>>>
a ="hello, iam shahd"
print(a.title())
# capitalize>>>>
b="hello, iam shahd"
print(b.capitalize())

# 14
first_name ='shahd'
s ='*********'
print('%s%s'%(s,first_name))
print('%s%s%s'%(s,first_name,s))
print('%s%s'%(first_name,s))


# 15
name_one = "SaMER"
name_two = "Abed"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())

# 16
print(name_one.isupper())
print(name_two.islower())

# 17
print(name_one.startswith('S'))
print(name_two.endswith('HD'))

# 18
msg1 = "I Love Python And Although I Love GSG with Zakaria"
print('Number of <Love> is:',msg1.count("Love"))
print('Number of <t> is:',msg1.count("t"))

# 19
msg2 = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg2.replace('%7','love',1))

# 20
test1 = "ZakZak"
test2 = "Zakaria"
test3 = "A war at Tarawa."
test4 = "madam"


