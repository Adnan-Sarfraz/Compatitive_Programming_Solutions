    

def fibonacci(numb):
    list_=[0,1]
    count=2
    if numb>2:
        while count<numb:
            sum=list_[-1]+list_[-2]
            list_.append(sum)
            count+=1
            print(list_)
    else:
        print("Number should be greator then 2")

fibonacci(7)
