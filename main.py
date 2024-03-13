def fib(n):
    contador = 0
    if n < 2:
        return n
    contador +=1
    return fib(n - 1) + fib(n - 2) 

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))