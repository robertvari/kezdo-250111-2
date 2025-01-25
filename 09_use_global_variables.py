NAME = "Tamás"

def say_hello():
    # import global NAME to local
    global NAME

    name = "Kriszta"

    # override global NAME
    NAME = "Csaba"
    print(NAME, name)

say_hello()
print(NAME)