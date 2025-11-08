def count_up_to(n):
    num = 1
    while num <= n:
        yield num
        num += 1

gen = count_up_to(5)

for x in gen:
    print(x)
