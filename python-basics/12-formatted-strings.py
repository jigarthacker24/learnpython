#formatted-strings

name = 'Johnny'
age = 55
print('hi ' + name + '. You are ' + str(age) + ' years old.')

#python >= v2
print('Hi {}. You are {} yours old.'.format(name, age))
print('Hi {1}. You are {0} yours old.'.format( age,name))

print('Hi {new_name}. You are {new_age} yours old.'.format( new_age=age,new_name=name))

#python3 ways f'str' called 'fstring' => formatted string
print(f'Hi {name}. You are {age} yours old.')
