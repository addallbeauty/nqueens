import time
# Fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
 
t1 = time.time()
n = int(input("Enter a number to find Fibonacci series using recursion: "))
print(fibonacci(n))
t2 = time.time()
recurr_time = t2-t1
print("Time for recursive fibonacci calculation is: ", recurr_time)



#Program using non-recursive method:
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    fibs = 1
    for i in range(3, n):
        fibs += i
    return fibs

t1 = time.time()
n = int(input("Enter a number to find Fibonacci series without using recursion: "))
print(fib(n))
t2 = time.time()
non_recurr_time = t2-t1
print("Time for non-recursive fibonacci calculation is: ", non_recurr_time)
