import math

def getCircleArea(radius):
    #_area = 3.14 * radius ** 2
    _area = math.pi * radius ** 2
    return _area

print(f'pi = {math.pi}')
radius = float(input('please enter radius [f]: '))
area = getCircleArea(radius)

def getCircleHekef(radius):
    pass # 2 * pi (3.14) * radius

def calcMalbenArea(width, height):
    pass # width * height

def calcMalbenHekef(width, height):
    pass # 2 * width + 2 * height
# input from user float radius -- print the hekef and area
# input from user width and height -- print the area and hekef