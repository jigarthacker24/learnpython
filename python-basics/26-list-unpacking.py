#26-list-unpacking.py

a,b,c,*other = [1,2,3,4,5,6,7,8,9]

print(a) #1
print(b) #2
print(c) #3
print(other) #[4, 5, 6, 7, 8, 9]

a,b,c,*other, last = [1,2,3,4,5,6,7,8,9]

print(a) #1
print(b) #2
print(c) #3
print(other) #[4, 5, 6, 7, 8]
print(last) #9
