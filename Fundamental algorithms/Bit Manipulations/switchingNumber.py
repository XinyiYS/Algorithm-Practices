
a = 10
b = 21

print(a,b)
# switching numbers without assignments
b = b ^ a 
a = a ^ b
b = b ^ a
print(a,b)