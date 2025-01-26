def recursive_function(n):
    n += 1
    print(f"Number: {n}")

    if n == 10:
        return
    
    recursive_function(n)

recursive_function(0)