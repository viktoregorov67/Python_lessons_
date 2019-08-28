# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print('help - получение справки')
    print('mkdir <dir_name> - создание директории')
    print('ping - тестовый ключ')
    print('cp <file_name> - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')

# Создание директории:
def make_dir():
    if not dir_name:
        print('Необходимо указать имя директории вторым параметром')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

# Копия указанного файла
def file_copy():
    if not file_name:
        print('Необходимо указать имя файла вторым параметром')
        return
    name_file = os.path.join(os.getcwd(), file_name)
    new_file = os.path.join(os.getcwd(), (name_file + '.copy'))
    if os.path.isfile(new_file) != True:
        shutil.copyfile(name_file, new_file)
        print(new_file + ' - создан')
    else:
        print('Файл уже скопирован')

#Удаление указанного файла
def file_del():
    if not file_name:
        print('Необходимо указать имя файла вторым параметром')
        return
    old_file = os.path.join(os.getcwd(), file_name)
    if os.path.isfile(old_file):
        confirm = input('Вы действительно хотите удалить указанный файл? y/n ')
        if confirm == 'y':
            os.remove(old_file)
            print(old_file + ' - данный файл удален')
        else:
            return
    else:
        print('Файл не найден')

#Смена директории на указанную
def change_dir():
    if not dir_name:
        print('Необходимо указать имя директории вторым параметром')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    print('Текущий каталог: ', os.getcwd())
    try:
        os.chdir(dir_path)
        print('Вы успешно перешли в директорию: ', format(dir_path))
    except FileNotFoundError:
        print('Такой директории не существует.', format(dir_path))

# Просмотр полного пути
def list_dir():
    print('Текущий каталог: ', os.path.dirname(__file__))

def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'cp': file_copy,
    'rm': file_del,
    'cd': change_dir,
    'ls': list_dir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
