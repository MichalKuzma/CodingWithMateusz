def factorial_last_digits(n):
    if n in [0,1]:
        return 1
        
    # if n >= 1000 then n! = 1 * 2 * ... * 1000 * 1001 * ... *  n
    if n >= 1000:
        return 0

    result = 1
    for i in range(2, n + 1):
        result = (result * i) % 100
    return result

def factorial(n):
    if n in [0,1]:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i # Same as: result = result * i
    
    return result

def factorial_recursive(n):
    if n in [0,1]:
        return 1
    
    # n! = n * (n-1)!
    return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    d = int(input())
    for i in range (d):
        n = int(input())
        last_digits = factorial_last_digits(n)
        print(last_digits // 10, last_digits % 10)

