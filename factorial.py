def factorial(number):
    if number == 0 or number == 1 :
        return 1
    else :
        return number  * factorial(number - 1)

def FactorialTrailingZeros(number):
    fact = factorial(number)
    count = fact + 1
    fact = fact /10
    return count