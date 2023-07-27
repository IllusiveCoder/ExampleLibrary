def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

# Test the function
num = 10
fib_numbers = fibonacci(num)
print(f"The Fibonacci sequence up to {num} terms: {fib_numbers}")