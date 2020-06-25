#22-list-methods.py

#List methods

basket = [1,3,2,4,5]

#print(len(basket))


#Adding at end => add item to the same list
basket.append(100)#[1, 3, 2, 4, 5, 100]
print(basket)

#insert at perticular index.
basket.insert(2,500)
print(basket)#[1, 3, 500, 2, 4, 5, 100]

#add list to the list
basket.extend([44,45])
print(basket)#[1, 3, 500, 2, 4, 5, 100, 44, 45]

#remove last item
popped_val = basket.pop()
print(basket)#[1, 3, 500, 2, 4, 5, 100, 44]
print(popped_val)#45

#remove item at index
popped_val = basket.pop(0)
print(basket)#[3, 500, 2, 4, 5, 100, 44]
print(popped_val)#1

#sort => sort the same list
basket.sort()
print(basket)#[2, 3, 4, 5, 44, 100, 500]

#remove value from list: removes first item found from list
basket.remove(500)
print(basket)#[2, 3, 4, 5, 44, 100]

#clear: clears the list and make it empty
basket.clear()
print(basket) #[]