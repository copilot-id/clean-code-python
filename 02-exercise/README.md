#### Exercise
- **Questions/Exercises:**
    - Add comments and documentation to the following code to improve its readability and maintainability.
    ```python
    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib_seq = [0, 1]
            for i in range(2, n):
                fib_seq.append(fib_seq[-1] + fib_seq[-2])
            return fib_seq

    print(fibonacci(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    ```
