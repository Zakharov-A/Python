
a = [1, 2]
b = [1, 2]

print(a == b) # True

print(a.__eq__(b)) # True

print(a.__eq__) 
# <method-wrapper '__eq__' of list object at 0x000002F031A6D100>

print(id(a)) # 2387164975360
print(hex(id(a))) # 0x22bce1ed100

