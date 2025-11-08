nums=[1,2,3,4,5]
def function(x):
    return x*x

print(nums ,"\n")
squared=list(map(function,nums))
print(squared)

print("--------------------------------FILTER-----------------------------\n")

numbers=[6,7,8,9,10,22,32,34,54,55,66,65,77]
def is_even(x):
    return x%2==0
print("Before filtraton")
print("\n",numbers,"\n")
even=list(filter(is_even,numbers))
print(even)