def erarly_return(number):
    if not isinstance(number, int):
        return "ERROR: Incorrect parameter."
    
    return f"Number is {number}"

print( erarly_return(10.123) )