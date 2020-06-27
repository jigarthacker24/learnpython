#24-list-methods-3.py

basket = ['e','c','b','d','a']

#create a new copy of a list
basket2 = basket.copy()#create a new copy of list

#inplace sorting
basket.sort()
print(basket)#['a', 'b', 'c', 'd', 'e']


#Get sorted array as new list
print(sorted(basket2))#['a', 'b', 'c', 'd', 'e']
print(basket2)#['e', 'c', 'b', 'd', 'a']

#Reverse the list
basket2.reverse()
print(basket2)#['a', 'd', 'b', 'c', 'e']