def main(a, b):

    def add_numbers():
        return a+b

    def divide_numbers():
        return a/b

    def multipy_numbers():
        return a*b
    
    add_result = add_numbers()
    divide_result = divide_numbers()
    multiply_result = multipy_numbers()

    return add_result, divide_result, multiply_result

final_result = main(10, 5)
print(final_result)