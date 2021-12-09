def factorial(n):
    assert n > 0 and int(n) == n, "The number must be begger than 0 and integer"
    if n in [0,1]:
        return 1
    return n * factorial(n-1)
   
def fib(n):
    assert n >= 0 and int(n) == n, "The number must be begger than 0 and integer"
    if n in [0,1]:
        return n
    return fib(n-1) + fib(n-2) 

def sod(n):
    if n == 0:
        return 0
    return (n % 10) + sod(n // 10)

def power(n, p):
    if p == 0:
        return 1
    return n * power(n, p-1)

def gdc(x, y):
    return n * power(n, p-1)


print(factorial(1)) 
print(fib(6)) 
print(sod(4)) 
print(power(3, 1)) 
