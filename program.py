def get_1():
    return 1 # breakout of the function
    print() # this command will never execute

def get_baribua( x ):
    print(x**2)
    return x**3

y = get_baribua(3)
print(f'y = {y}')
print(get_1())
x = get_1()
print(f'function result: {get_1()}')
get_1()


