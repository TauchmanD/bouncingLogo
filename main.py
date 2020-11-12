import time
import os

global tempo
tempo = [1, 1]
global bounces
bounces = 0
global corners
corners = 0
global array
array = []


def sleep(x):
    """
    Pozadtaví kód
    :param x: Počet sekund pozastavení
    :return:
    """
    time.sleep(x)


def create_array(array, size_y, size_x):
    """
    Vytvoří 2d pole
    :param array: Pole ze kterého se vytvoří 2d pole
    :param size_y: Velikost osy Y
    :param size_x: Velikost osy X
    :return:
    """
    for y in range(size_y):
        array.append([])
        for x in range(size_x):
            array[y].append('-')


def print_array(array):
    """
    Vykreslí pole v hezkém formátu
    :param array: Pole, které chceme vykreslit
    :return:
    """
    size_y = len(array)
    size_x = len(array[0])
    for y in range(size_y):
        for x in range(size_x):
            print(array[y][x], end="")
        print("")


def set_position(array, position_y, position_x):
    """
    Nastaví novou pozici odrážejícího se objektu
    :param array: Pole, kde chceme změnit pozici
    :param position_y: Pozice osy Y
    :param position_x: Pozice osy X
    :return:
    """
    if get_position(array) == 0:
        array[position_y][position_x] = '*'
    else:
        coords = get_position(array)
        array[coords[0]][coords[1]] = "-"
        array[position_y][position_x] = '*'


def get_position(array):
    """
    Získá aktuální pozici odrážejícího se objektu
    :param array: Pole, kde se nachází objekt
    :return: Pozice objektu
    """
    size_y = len(array)
    size_x = len(array[0])
    for y in range(size_y):
        for x in range(size_x):
            if array[y][x] == '*':
                return y, x
    return 0


def set_tempo(array, coords):
    """
    Nastaví nové tempo o které se objekt pohybuje
    :param array: Pole s objektem
    :param coords: Souřadnice objektu
    :return: O co se objekt odrazil
    """
    if coords == (0, 0) or coords == (0, len(array[0]) - 1) or coords == (len(array) - 1, 0) or coords == (
            len(array) - 1, len(array[0]) - 1):
        tempo[0], tempo[1] = -tempo[0], -tempo[1]
        sleep(1)
        return 'corner'
    elif coords[0] == len(array) - 1 or coords[0] == 0:
        tempo[0], tempo[1] = -tempo[0], tempo[1]
        return 'bounce'

    elif coords[1] == len(array[0]) - 1 or coords[1] == 0:
        tempo[0], tempo[1] = tempo[0], -tempo[1]
        return 'bounce'
    return False


def print_bouncing():
    """
    Vykreslí HUD
    :return:
    """
    clear()
    print_array(array)
    print()
    print("tempo[y/x]: " + str(tempo))
    print("Bounces: " + str(bounces))
    print("Corners: " + str(corners))


def print_corner():
    """
    Animace zasažení rohu
    :return:
    """
    for i in range(3):
        clear()
        print("          _____                  _______                  _____                   _____                    _____                    _____          ")
        print("         /\    \                /::\    \                /\    \                 /\    \                  /\    \                  /\    \         ")
        print("        /::\    \              /::::\    \              /::\    \               /::\____\                /::\    \                /::\    \        ")
        print("       /::::\    \            /::::::\    \            /::::\    \             /::::|   |               /::::\    \              /::::\    \       ")
        print("      /::::::\    \          /::::::::\    \          /::::::\    \           /:::::|   |              /::::::\    \            /::::::\    \      ")
        print("     /:::/\:::\    \        /:::/~~\:::\    \        /:::/\:::\    \         /::::::|   |             /:::/\:::\    \          /:::/\:::\    \     ")
        print("    /:::/  \:::\    \      /:::/    \:::\    \      /:::/__\:::\    \       /:::/|::|   |            /:::/__\:::\    \        /:::/__\:::\    \    ")
        print("   /:::/    \:::\    \    /:::/    / \:::\    \    /::::\   \:::\    \     /:::/ |::|   |           /::::\   \:::\    \      /::::\   \:::\    \   ")
        print("  /:::/    / \:::\    \  /:::/____/   \:::\____\  /::::::\   \:::\    \   /:::/  |::|   | _____    /::::::\   \:::\    \    /::::::\   \:::\    \  ")
        print(" /:::/    /   \:::\    \|:::|    |     |:::|    |/:::/\:::\   \:::\____\ /:::/   |::|   |/\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\  ")
        print("/:::/____/     \:::\____\:::|____|     |:::|    /:::/  \:::\   \:::|    /:: /    |::|   /::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    | ")
        print("\:::\    \      \::/    /\:::\    \   /:::/    /\::/   |::::\  /:::|____\::/    /|::|  /:::/    /\:::\   \:::\   \::/    /\::/   |::::\  /:::|____|  ")
        print(" \:::\    \      \/____/  \:::\    \ /:::/    /  \/____|:::::\/:::/    / \/____/ |::| /:::/    /  \:::\   \:::\   \/____/  \/____|:::::\/:::/    /   ")
        print("  \:::\    \               \:::\    /:::/    /         |:::::::::/    /          |::|/:::/    /    \:::\   \:::\    \            |:::::::::/    /    ")
        print("   \:::\    \               \:::\__/:::/    /          |::|\::::/    /           |::::::/    /      \:::\   \:::\____\           |::|\::::/    /     ")
        print("    \:::\    \               \::::::::/    /           |::| \::/____/            |:::::/    /        \:::\   \::/    /           |::| \::/____/      ")
        print("     \:::\    \               \::::::/    /            |::|  ~|                  |::::/    /          \:::\   \/____/            |::|  ~|            ")
        print("      \:::\    \               \::::/    /             |::|   |                  /:::/    /            \:::\    \                |::|   |             ")
        print("       \:::\____\               \::/____/              \::|   |                 /:::/    /              \:::\____\               \::|   |            ")
        print("        \::/    /                ~~                     \:|   |                 \::/    /                \::/    /                \:|   |            ")
        print("         \/____/                                         \|___|                  \/____/                  \/____/                  \|___|            ")
        sleep(0.5)
        clear()
        sleep(0.5)


def user_input():
    """
    Vstup od uživatele
    :return:
    """
    while True:
        size_y = int(input("Zadej velikost y: "))
        size_x = int(input("Zadej velikost x: "))
        if not (size_y <= 1 or size_x <= 1):
            break
        print("Souřadnice se nesmí rovnat 1!")
    create_array(array, size_y, size_x)
    start = int((size_y * 0.75) // 1)
    set_position(array, start, 1)


def move():
    """
    Pohyb objektu
    :return:
    """
    coords = get_position(array)
    new_y = coords[0] + tempo[0]
    new_x = coords[1] + tempo[1]
    set_position(array, new_y, new_x)


clear = lambda: os.system('cls')

user_input()
while True:
    move()
    print_bouncing()
    coords = get_position(array)
    result = set_tempo(array, coords)
    if result == 'bounce':
        bounces += 1
    elif result == 'corner':
        print_corner()
        corners += 1
    sleep(0)