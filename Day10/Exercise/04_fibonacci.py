# Exercise : To Print Fibonacci series upto Nth Term

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Enter the number of terms: "))
fib_sequence = fibonacci(n)
print(f"Fibonacci sequence up to {n} terms:")
print(fib_sequence)
