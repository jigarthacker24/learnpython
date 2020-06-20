# string-indexes
# access individual character of a string

name = 'Jigar Thacker'

print(name[3]) #a

#slices => [start:stop]
#slices => [start:stop:stepover]
#slices => [start:]
print(name[0:5]) #Jigar
print(name[3:5]) #ar

print(name[3:]) #ar Thacker
print(name[:5]) #Jigar

print(name[:]) #Jigar Thacker
print(name[0:])#Jigar Thacker

print(name[0:8:1])#Jigar Th
print(name[0:8:2])#JgrT

print(name[::2])#JgrTakr
print(name[::3])#JaTcr

#minus 
print(name[-1])#r
print(name[-2])#e
print(name[:-1])#Jigar Thacke
print(name[:-5])#Jigar Th

#reverse
print(name[::-1])#rekcahT ragiJ
print(name[::-2])#rkaTrgJ
