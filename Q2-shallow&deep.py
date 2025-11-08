import copy
list=[[1,2,3],[4,5,6]]
shallow_coppy=copy.copy(list)
deep_coppy=copy.deepcopy(list)
list[0][0]=99
print("shallow coppy  --> ",shallow_coppy)
print("orignal list   --> ", list)
print("Deep coppy     -->", deep_coppy)