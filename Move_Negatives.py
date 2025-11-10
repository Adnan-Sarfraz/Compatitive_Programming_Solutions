print("---------------------------------------------MOVE NEGATIVES TO LEFT----------------------------------------------")
array = [20, -1, 3, 2, -7, -5, 11, 6]
def move_negative(arr):
    left=0
    right=len(arr)-1
    while left<=right:
        if arr[left]<0:
            left+=1
        elif arr[right]>0:
            right-=1
        else:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    return arr
  
print(move_negative(array))

print("\n---------------------------------------------MOVE NEGATIVES TO RIGHT----------------------------------------------")
arrayy = [20, -1, 3, 2, -7, -5, 11, 6]
def negative_move(aarr):
    l=0
    R=len(aarr)-1
    while l<=R:
        if aarr[l]>0:
            l+=1
        elif aarr[R]<0:
            R-=1
        else:
            aarr[R],aarr[l]=aarr[l],aarr[R]
    return aarr

print(negative_move(arrayy))