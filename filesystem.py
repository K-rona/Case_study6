import os

MENU = "1. Просмотр каталога\n" \
       "2. На уровень вверх\n" \
       "3. На уровень вниз\n" \
       "4. Количество файлов\n" \
       "5. Размер текущего каталога (в байтах)\n" \
       "6. Поиск файла\n" \
       "7. Выход из программы"


def AcceptCommand():
    command = input('Выберите пункт меню: ')

    while command not in ['1','2','3','4','5','6','7']:
        if command not in ['1','2','3','4','5','6','7']:

            print("Неверная команда! Введите другой номер команды")

        command = input('Выберите пункт меню: ')

    return int(command)


def MoveUp():
    dir = os.getcwd()
    i = len(dir) - 1
    while dir[i] != '\\':
        i = i - 1
    os.chdir(dir[:i])

def CountFiles(path):

    summ_file = 0
    file_list = os.listdir(path)

    for i in file_list:
        if os.path.isfile(path + "\\" + i):
            summ_file +=1
        else:
            summ_file += CountFiles(path + "\\" + i)
    return summ_file

def FindFiles(target, path):

    list_path = []
    all_file_list = os.listdir(path)

    for i in all_file_list:
        if os.path.isfile(path + "\\" + i) and target in i:
            list_path.append(path + "\\" + i)

        elif os.path.isdir(path + "\\" + i):
            if FindFiles(target,path + "\\" + i):
                list_path.extend(FindFiles(target,path + "\\" + i))

    return list_path

def Lookthrough(CurrentDir):

    content = os.listdir(CurrentDir)

    for element in content:

        if os.path.isfile(CurrentDir + "/" + element):
            print(element, "," + "type = file")

        if os.path.isdir(CurrentDir + "/" + element):
            print(element, "," + "type = dir")


def MoveDown(CurrentDir):

    test = False

    while not test:

        subdirectory_name = input("Введите название подкаталога: ")
        test = os.path.exists(CurrentDir + "/" + subdirectory_name)

        if not test:
            print("Некорректное название каталога")

    NewDir = CurrentDir + "/" + subdirectory_name
    os.chdir(NewDir)


def CountBytes(CurrentDir):

    content = os.listdir(CurrentDir)
    print(content)
    summ_bytes = 0

    for i in content:

        if os.path.isfile(CurrentDir + "/" + i):
            summ_bytes += os.path.getsize(CurrentDir + "/" + i)

        if os.path.isdir(CurrentDir + "/" + i):
            summ_bytes += CountBytes(CurrentDir + "/" + i)

    return summ_bytes

def RunCommand(command):

    CurrentDir = os.getcwd()

    if command == 1:
        Lookthrough(CurrentDir)

    if command == 2:
        MoveUp(CurrentDir)

    if command == 3:
        MoveDown(CurrentDir)

    if command == 4:
        CountFiles(CurrentDir)

    if command == 5:
        CountBytes(CurrentDir)

    if command == 6:
        target, path = input("Выберите target и path").split()
        FindFiles(target,path)


def main():
    while True:

        print(os.getcwd())
        print(MENU)
        command = AcceptCommand()

        if command == 7:
            print('Работа программы завершена.')
            break

        RunCommand(command)


if __name__ == '__main__':
    main()
