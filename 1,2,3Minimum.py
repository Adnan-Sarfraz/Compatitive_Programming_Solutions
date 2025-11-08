list_ = [1, 44, 22, 4, 2, 1, 6]
m1=float("inf")
m2=float("inf")
m3=float("inf")
for num in list_:
    if num<m1:
       m3=m2
       m2=m1
       m1=num
    elif num<m2 and num!=m1:
        m3=m2
        m2=num
    elif num<m3 and num!=m2 and num!=m1:
        m3=num

print("First minimum->  ", m1)
print("Second minimum-> ", m2)
print("Third minimum->  ", m3)
