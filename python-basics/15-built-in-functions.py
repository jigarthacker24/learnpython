#15-built-in-functions.py

#basic functions
#str()
#int()
#print()
#abs()
#round()
#type()

#string function
print(len('Hello'))#5

quote = 'to be or not to be'

print (quote.upper())#TO BE OR NOT TO BE

print(quote.capitalize())#To be or not to be

print(quote.find('be'))#3 => index first occurence of 'be

print(quote.replace('be','me'))# me or not to me

#quote does not get alterred
print(quote)#to be or not to be

quote2 = quote.replace('be','me')
print(quote2)# me or not to me
