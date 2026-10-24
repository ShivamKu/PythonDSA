num1 =11
num2 = num1
"""
11(obj and address) <- num1 and <- num2 also pointing to same address
"""
print("Before num2 value is updated:")
print("num1=", num1)
print("num2=",num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

num2 = 22
"""
Now 11(obj, add) <- num1 and 22(obj,add) <- num2
"""
print("\nAfter num2 value updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# dict data type
dict1 = {'value':11}
dict2 = dict1

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] =22
print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))