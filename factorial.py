def factorial(n):
    if not isinstance(n, int) or n < 0:
        print("only pos int")
        return None
    else:
        result = 1
        for i in range(n, 0, -1):
            result *= i
        return result

print(factorial(6))