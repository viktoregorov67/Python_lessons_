# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import time

# Создаем новую директорию
def make_dir(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.makedirs(dir_path)
        print('Директория создана', format(dir_path))
    except FileExistsError:
        print('Такая директория уже существует', format(dir_path))

# Удаление директории
def del_dir(name):
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.removedirs(dir_path)
        print('Директория удалена', format(dir_path))
    except FileNotFoundError:
        print('Такая директория не найдена или уже удалена', format(dir_path))

# Создаем директории dir_1 - dir_9 в текущей папке и затем удаляем их
if __name__ == '__main__':
    num = 1
    while num < 10:
        dir_name = 'dir_' + str(num)
        make_dir(dir_name)
        num += 1

    time.sleep(5)
    num = 1
    while num < 10:
        dir_name = 'dir_' + str(num)
        del_dir(dir_name)
        num += 1

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    print('Текущая директория: ', os.path.dirname(__file__))
    folders = os.listdir()
    print('Папки в текущей директории:')
    for index, element in enumerate(folders, start=1):
        if os.path.isdir(element):
            print('{}'.format(element))

if __name__ == '__main__':
    list_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys
import shutil
#
def copy_current_file():
    name_file = os.path.realpath(__file__)
    new_file = name_file +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copyfile(name_file, new_file)
        print(new_file + ' - создан')
    else:
        print('Файл уже скопирован')

if __name__ == '__main__':
    print(copy_current_file())

