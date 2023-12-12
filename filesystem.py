import os
import Text_Ru


def accept_command():
    
    command = input(Text_Ru.MENU_ITEM)

    while command not in ['1', '2', '3', '4', '5', '6', '7']:
        if command not in ['1', '2', '3', '4', '5', '6', '7']:

            print(Text_Ru.WRONG_COMMAND)

        command = input(Text_Ru.MENU_ITEM)

    return int(command)


def move_up():
    
    directory = os.getcwd()
    i = len(directory) - 1
    
    while directory[i] != '\\':
        i = i - 1
    os.chdir(directory[:i])


def count_files(path):

    summ_file = 0
    file_list = os.listdir(path)

    for i in file_list:
        if os.path.isfile(path + "\\" + i):
            summ_file += 1
        else:
            summ_file += count_files(path + "\\" + i)
    return summ_file


def find_files(target, path):

    list_path = []
    all_file_list = os.listdir(path)

    for i in all_file_list:
        if os.path.isfile(path + "\\" + i) and target in i:
            list_path.append(path + "\\" + i)

        elif os.path.isdir(path + "\\" + i):
            if find_files(target, path + "\\" + i):
                list_path.extend(find_files(target, path + "\\" + i))

    return list_path


def look_through(current_dir):

    content = os.listdir(current_dir)

    for element in content:

        if os.path.isfile(current_dir + "/" + element):
            print(element, "," + "type = file")

        if os.path.isdir(current_dir + "/" + element):
            print(element, "," + "type = dir")


def move_down(current_dir):

    test = False

    while not test:

        subdirectory_name = input(Text_Ru.SUBDIRECTORY_NAME)
        test = os.path.exists(current_dir + "/" + subdirectory_name)

        if not test:
            print(Text_Ru.ERROR_SUBDIRECTORY)

    new_dir = current_dir + "/" + subdirectory_name
    os.chdir(new_dir)


def count_bytes(current_dir):

    content = os.listdir(current_dir)
    summ_bytes = 0

    for i in content:

        if os.path.isfile(current_dir + "/" + i):
            summ_bytes += os.path.getsize(current_dir + "/" + i)

        if os.path.isdir(current_dir + "/" + i):
            summ_bytes += count_bytes(current_dir + "/" + i)

    return summ_bytes


def run_command(command):

    current_dir = os.getcwd()

    if command == 1:
        look_through(current_dir)

    if command == 2:
        move_up()

    if command == 3:
        move_down(current_dir)

    if command == 4:
        print(count_files(current_dir))

    if command == 5:
        print(count_bytes(current_dir))

    if command == 6:
        
        target, path = input(Text_Ru.FINDING_FILES).split()
        find_file = find_files(target, path)
           
        if find_file:
            for i in find_file:
                print(i)
            else:
                print(Text_Ru.FILE_ERROR)


def main():
    
    while True:

        print(os.getcwd())
        print(Text_Ru.MENU)
        command = accept_command()

        if command == 7:
            print(Text_Ru.END_OF_PROGRAM)
            break

        run_command(command)


if __name__ == '__main__':
    main()
    
