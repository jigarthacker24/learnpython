#type conversion

#convert to string
print(type(str(100)))

#string to int
print(type(int(str(100))))

# type convert
a = str(100)
b = int(a)
c = type(b)

print(type(c)) #type of type is <class 'type'>
print(c)