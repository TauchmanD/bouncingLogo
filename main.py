import time
import os


global tempo
tempo = [1, 1]
global bounces
bounces = 0
global corners
corners = 0


def sleep(x):
    time.sleep(x)


def create_array(array, size_y, size_x):
    for y in range(size_y):
        array.append([])
        for x in range(size_x):
            array[y].append('-')


def print_array(array):
    size_y = len(array)
    size_x = len(array[0])
    for y in range(size_y):
        for x in range(size_x):
            print(array[y][x], end="")
        print("")


def set_position(array, position_y, position_x):
    if get_position(array) == 0:
        array[position_y][position_x] = '*'
    else:
        coords = get_position(array)
        array[coords[0]][coords[1]] = "-"
        array[position_y][position_x] = '*'


def get_position(array):
    size_y = len(array)
    size_x = len(array[0])
    for y in range(size_y):
        for x in range(size_x):
            if array[y][x] == '*':
                return y, x
    return 0


def set_tempo(array, coords):
    if coords == (0, 0) or coords == (0, len(array[0])-1) or coords == (len(array)-1, 0) or coords == (len(array)-1, len(array[0])-1):
        tempo[0], tempo[1] = -tempo[0], -tempo[1]
        return 'corner'
    elif coords[0] == len(array) - 1 or coords[0] == 0:
        tempo[0], tempo[1] = -tempo[0], tempo[1]
        return 'bounce'

    elif coords[1] == len(array[0]) - 1 or coords[1] == 0:
        tempo[0], tempo[1] = tempo[0], -tempo[1]
        return 'bounce'
    return False


clear = lambda: os.system('cls')
array = []
while True:
    size_y = int(input("Zadej velikost y: "))
    size_x = int(input("Zadej velikost x: "))
    if not(size_y <=1 or size_x <= 1):
        break
    print("Souřadnice se nesmí rovnat 1!")
create_array(array, size_y, size_x)
start = int((size_y * 0.75) // 1)
set_position(array, start, 1)
while True:
    clear()
    print_array(array)
    print()
    print("tempo[y/x]: " + str(tempo))
    print("Bounces: " + str(bounces))
    print("Corners: " + str(corners))
    coords = get_position(array)
    result = set_tempo(array, coords)
    if result == 'bounce':
        bounces+=1
    elif result == 'corner':
        corners +=1
    new_y = coords[0] + tempo[0]
    new_x = coords[1] + tempo[1]
    set_position(array, new_y, new_x)

    sleep(0.125)

