from test2 import *






test2_list = [128,2,4,16,2,128,64,4,7,4,64]
x = remove_duplicate(test2_list)
a = product(256,x)

b = {k:v for v,k in enumerate(test2_list)}

print(a, end=" ")
print(*(b[k] for k in a))







# print(a)
# print(x)

