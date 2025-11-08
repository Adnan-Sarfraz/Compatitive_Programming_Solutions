#----------------------WITHOUT ARGUMENTS--------------------------------
# def my_decorator(func):
#     def wrapper():
#         print("\nASSALAMUALAIKUM!")
#         func()
#         print("\nALLAH HAFIZ!")
#     return wrapper

# @my_decorator
# def greeting():
#     print("\nHELLO MY NAME IS ADNAN SARFRAZ AND I AM LOOKING FOR JOB")

# greeting()



#----------------------WITH ARGUMENTS------------------------------------
def decorator(func):
    def wrapper(a,b):
        print("BEFORE TAKING SUM")
        result=func(a,b)
        print("AFTER TAKING THE SUM")
    return wrapper

@decorator
def sum(a,b):
    print(a+b)

sum(10,2)