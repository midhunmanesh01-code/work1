def fib(n):
    list=[]
    a, b = 0, 1
    for i in range(n):
        list.append(a)
        a, b = b, a + b
    return list