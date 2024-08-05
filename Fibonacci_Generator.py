def fibonacci(n):
    """
    Returns the first n Fibonacci numbers
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def fibonacci_recursive(n):
    """
    Returns the nth Fibonacci number using recursion
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    """
    Returns the nth Fibonacci number using iteration
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# Test the functions
print("Fibonacci sequence (first 10 numbers):")
print(fibonacci(10))

print("\n10th Fibonacci number (recursive):")
print(fibonacci_recursive(10))

print("\n10th Fibonacci number (iterative):")
print(fibonacci_iterative(10))
