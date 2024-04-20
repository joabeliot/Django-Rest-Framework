def decorator(f):
    print(f())
    return f

@decorator
def decoratedFunction():
    return "nigga"

decoratedFunction()