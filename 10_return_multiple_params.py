def calculate_numbers(a, b):
    # this always returns a tuple
    return a + b, a / b, a * b

result = calculate_numbers(10, 5)
print(  result, type(result)  )