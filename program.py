import math

def getCircleArea(r):
    _area = math.pi * r ** 2
    return _area

def getCircleHekef(r):
    _hekef = 2 * math.pi * r
    return _hekef

print(f'pi = {math.pi}')
radius = float(input('please enter radius [f]: '))
circle_area = getCircleArea(radius)
circle_hekef = getCircleHekef(radius)
print(f'circle radius {radius}, area: {circle_area}')
print(f'circle radius {radius}, hekef: {circle_hekef}')

def calcMalbenArea(width, height):
    return width * height

def calcMalbenHekef(width, height):
    return 2 * width + 2 * height

w = float(input('please enter malben width [f]: '))
h = float(input('please enter malben height [f]: '))
print(f'malben area: {calcMalbenArea(w, h)}')
print(f'malben hekef: {calcMalbenHekef(w, h)}')

def even_or_odd(x):
    # return 'even' if x % 2 == 0 else 'odd'
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'
print(f'8 is {even_or_odd(8)}')
print(f'7 is {even_or_odd(7)}')

def get_factorial(x):
    atz = 1
    for i in range(2, x + 1):
        atz *= i
    return atz

print(f'5! = {get_factorial(5)}')

def check_equal(x, y = 0):
    # return x == y
    if x == y:
        return True
    else:
        return False
    # get two parameters
    # if they are equal return True otherwise False
    # if only 1 number was sent then compare it to zero

print(f'1 == 1 {check_equal(1, 1)}')
print(f'2 == 1 {check_equal(2, 1)}')
print(f'3 == 0 {check_equal(3)}')
print(f'0 == 0 {check_equal(0)}')

def get_full_name(fname = 'John', lname = 'Doe'):
    # get two parameters: fname , lname
    # if i.e. avi levi was sent return 'avi levi'
    # if i.e. only fname was send return 'avi doe'
    # if t.e. none was send return 'john doe'
    return f'{fname} {lname}'

