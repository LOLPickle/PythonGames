import random
import time
from colorama import init, Fore, Back, Style
import keyboard

# Ініціалізація
init()

import random

def generate_maze(width, height):
    # Ініціалізація сітки
    maze = [["#" for _ in range(width)] for _ in range(height)]
    visited = [[False for _ in range(width)] for _ in range(height)]

    # Початкова точка
    start_x, start_y = 1, 1
    maze[start_y][start_x] = " "
    visited[start_y][start_x] = True

    # Напрямки руху: (dx, dy)
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]

    def is_valid(x, y):
        return 0 < x < width - 1 and 0 < y < height - 1 and not visited[y][x]

    def carve_path(x, y):
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                maze[y + dy // 2][x + dx // 2] = " "  # Відкриваємо стіну між клітинками
                maze[ny][nx] = " "  # Відкриваємо нову клітинку
                visited[ny][nx] = True
                carve_path(nx, ny)

    # Запуск генерації лабіринту
    carve_path(start_x, start_y)

    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

# Параметри лабіринту
width, height = 21, 21  # Розміри лабіринту (мають бути непарними)

# Мапа (двовимірний список)
simple_map = generate_maze(width, height)
# Початкова позиція
x, y = 1, 1  # Позиція на карті (x, y)

initial_map = [row.copy() for row in simple_map]

def Game():
    global x, y, simple_map, initial_map
    # Очищаємо консоль
    print("\033c", end="")  # ANSI escape code для очищення екрану
    print("Натисніть 'q' для виходу...")

    # Основний цикл гри
    while True:
        print("\033c", end="")
        if keyboard.is_pressed('right') and x < len(simple_map[0]) - 1:  # Перевірка меж карти
            if simple_map[y][x + 1] != '#':  # Якщо справа немає стіни
                x += 1  # Рух вправо
        elif keyboard.is_pressed('left') and x > 0:  # Перевірка меж карти
            if simple_map[y][x - 1] != '#':  # Якщо зліва немає стіни
                x -= 1  # Рух вліво
        elif keyboard.is_pressed('up') and y > 0:  # Перевірка меж карти
            if simple_map[y - 1][x] != '#':  # Якщо зверху немає стіни
                y -= 1  # Рух вгору
        elif keyboard.is_pressed('down') and y < len(simple_map) - 1:  # Перевірка меж карти
            if simple_map[y + 1][x] != '#':  # Якщо знизу немає стіни
                y += 1  # Рух вниз

        # Перевіряємо натискання клавіші 'q' для виходу
        if keyboard.is_pressed('q'):
            print("\033c", end="")  # Очистка консолі перед виходом
            return  # Завершити гру

        # Копіюємо початкову мапу для відновлення її стану
        current_map = [row.copy() for row in initial_map]

        # Встановлюємо поточну позицію гравця як '@'
        current_map[y][x] = '@'

        # Виводимо нову мапу
        for row in current_map:
            print(''.join(row))  # Виводимо кожен рядок карти як рядок символів

        time.sleep(0.1)  # Зменшена затримка для кращої чутливості



def main():
    current_option = 1  # Початковий вибір меню
    options = 3  # Кількість пунктів меню

    print("\033c", end="")  # Очищення консолі

    while True:
        print("\033c", end="")  # Очищення екрану
        print('   ____     _____   ___    __   _____    _____    _       ______ ')
        print('  / ___|   /  _  \  ||\\    ||  / ____|  /  _   \ | |     |  ____|')
        print(' | |      |  | |  | || \\   || | |____  |  | |  | | |     | |__   ')
        print(' | |      |  | |  | ||  \\  ||  \___  | |  | |  | | |     |  __|  ')
        print(' | |___   |  |_|  | ||   \\ ||   ___| | |  |_|  | | |____ | |____ ')
        print('  \____|   \_____/  ||    \\||  /_____/  \_____/  |______||______|\n')

        # Відображення пунктів меню
        print("> play" if current_option == 1 else "  play")
        print("> settings                                                     ↑   " if current_option == 2 else "  settings                                                     ↑   ")
        print("> exit                                                       ← ↓ →" if current_option == 3 else "  exit                                                       ← ↓ →")

        # Обробка натискань клавіш
        if keyboard.is_pressed('up'):
            current_option -= 1
            if current_option < 1:
                current_option = options  # Переходить до останнього пункту
            time.sleep(0.2)  # Затримка для стабільності

        elif keyboard.is_pressed('down'):
            current_option += 1
            if current_option > options:
                current_option = 1  # Переходить до першого пункту
            time.sleep(0.2)  # Затримка для стабільності

        elif keyboard.is_pressed('enter'):  # Вибір пункту меню
            if current_option == 1:
                print("Запуск гри...")
                time.sleep(1)
                print("\033c", end="")
                Game()
                break
            elif current_option == 2:
                print("Відкриття налаштувань...")
                time.sleep(1)
                break
            elif current_option == 3:
                print("Вихід з програми...")
                time.sleep(1)
                exit()
        
        time.sleep(0.1)
    


    

if __name__ == "__main__":
    main()


