#23-list-methods-2.py

basket = ['a','b','c','d','e']


#index of list item
print(basket.index('d'))#3

#ValueError if item not found in the list
#print(basket.index('5')) #ValueError: '5' is not in list

#index with start and end index
print(basket.index('d',0,4))#3

#item in list
print('d' in basket)#True
print('x' in basket)#False

print('i' in 'Hi my name is Anna')#True

#item ouccrence count in list
print(basket.count('d'))#1

