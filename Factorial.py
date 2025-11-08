def factorial(num):
    orignal=num
    result=1
    while num>0:
        result = result * num
        num-=1
        
    print(f"Factorial of{orignal} is-> ", result )

factorial(3)