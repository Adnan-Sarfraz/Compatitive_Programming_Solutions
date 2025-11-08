list_ = [1, 44, 22, 4, 2, 1, 6]
max1=-2
max2=-1

for num in list_:
    if num>max1:
        max1=num
    #elif num>max2 and num!=max1:
       # max2=num

print("first highest ",max1)
print("second highest ",max2)