# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

#Interesting this acts like a main method for a class. Python is very flexible in which functions methods and classes are defined.
#This can be really cool or not cool at all.
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))