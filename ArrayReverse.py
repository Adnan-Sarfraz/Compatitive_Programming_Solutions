list=[1,2,3,4,5]
start=0
end=len(list)-1
print("Before reverssl", list)
while start<end:
    temp=list[start]
    list[start]=list[end]
    list[end]=temp
    start+=1
    end-=1

print("After reverssl\n", list)