def factorial(n):

    if n > 1:
        n = n*factorial(n-1)
    print(n)
    return n

factorial(5)
