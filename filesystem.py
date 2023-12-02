import os

MENU = "1. Просмотр каталога\n" \
       "2. На уровень вверх\n" \
       "3. На уровень вниз\n" \
       "4. Количество файлов\n" \
       "5. Размер текущего каталога (в байтах)\n" \
       "6. Поиск файла\n" \
       "7. Выход из программы"


def Accept_command():



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
        FindFiles(target,path)


def Lookthrough(CurrentDir):

    content = os.listdir(CurrentDir)

    for element in content:

        if os.path.isfile(CurrentDir + "/" + element):
            print(element, "," + "type = file")

        if os.path.isdir(CurrentDir + "/" + element):
            print(element, "," + "type = file")


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




def main():
    while True:

        print(os.getcwd())
        print(MENU)
        command = acceptCommand()

        if command == 7:
            print('Работа программы завершена.')
            break

        RunCommand(command)


if __name__ == '__main__':
    main()
