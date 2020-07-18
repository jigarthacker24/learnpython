#25-common-list-pattern.py

basket = ['a','b','c','d','e']

#Reverse as Copy
rlist = basket[::-1]
print(rlist)


#Generate a list from range
print(range(15))#range(0, 15)
list2 = list(range(20)) 
print(list2)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

new_list = list(range(1,15))
print(new_list)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#.join

sentense = '!'
new_sen = sentense.join(['hi','my','name', 'is', 'Jigar'])
print(new_sen)#hi!my!name!is!Jigar

new_sen = ''.join(['hi','my','name', 'is', 'Jigar'])
print(new_sen)#himynameisJigar

new_sen = ' '.join(['hi','my','name', 'is', 'Jigar'])
print(new_sen)#hi my name is Jigar