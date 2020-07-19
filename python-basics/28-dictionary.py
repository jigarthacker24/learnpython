#28-dictionary.py
#unordered key:value pair internallly

my_dict = {
    'a': 1,
    'b': 2,
    'x': 3
}

print(my_dict)#{'a': 1, 'b': 2, 'x': 3}


my_dict = {
    'a': [1,2,3],
    'b': 'hello',
    'x': 3
}
print(my_dict)#{'a': [1, 2, 3], 'b': 'hello', 'x': 3}
print(my_dict['a'][1])#2

my_list = [
    {
    'a': [1,2,3],
    'b': 'hello',
    'x': 3
},
{
    'a': [4,5,6],
    'b': 'hello',
    'x': False
}
] 

print(my_list[1]['a'][2])#6