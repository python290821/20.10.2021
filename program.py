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
    pass # width * height

def calcMalbenHekef(width, height):
    pass # 2 * width + 2 * height
# input from user float radius -- print the hekef and area
# input from user width and height -- print the area and hekef

def even_or_odd(x):
    pass # return 'even' if even or 'odd'

def get_factorial(x):
    pass # return factorial atzret . x = 5 => 1 * 2 * 3 * 4 * 5

def check_equal():
    # get two parameters
    # if they are equal return True otherwise false
    # if only 1 number was sent then compare it to zero
    pass #

def get_full_name():
    # get two parameters: fname , lname
    # if i.e. avi levi was sent return 'avi levi'
    # if i.e. only fname was send return 'avi doe'
    # if t.e. none was send return 'john doe'
    pass
