#20-list-slice.py

amazon_cart = [
'notebooks',
'sunglasses',
'toys',
'grapes'
]

amazon_cart[0] = 'laptop'



new_cart = amazon_cart[:]
amazon_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
