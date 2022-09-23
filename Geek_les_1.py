import os
import psutil
import pprint
import sys
import shutil
quastion = ''
while quastion != 'w':
    quastion = input("Хотите ли вы поработать?(Y/N/w)")
    if quastion == "Y":
        print("Что именно вы совуршить?")
        print("[1] - показать содержимое папки?")
        print("""[2] - вывести информацию о системе:
                 Имя текущей дерриктории;
                 Тип операционной системы;
                 Кодировку файловой системы;
                 Количество CPU;
                 Логин пользователя
        """)
        print("[3] - выведу список процессов")
        print("[4] - сделаю копию файлов имеющихся в текущей дерриктории")
        print("[5] - продублирую файл, имя которого укажете")
        print("[6] - удалю все файлы с окончанием '.dupl' в указанной вами дирректории")
        choice = int(input("Выберите один из вариантов:"))
        if choice == 1:
            print(os.listdir())
        if choice == 2:
            print(os.getcwd())
            print(sys.platform)
            print(sys.getdefaultencoding())
            print(psutil.cpu_count())
            print(os.getlogin())
        if choice == 3:
            pprint.pprint(psutil.pids())
        if choice == 4:
            i = 0
            list = os.listdir()
            while i < len(list):
                new_files = list[i] + ".dubl"
				if os.path.isfile(list[i]) is True:
					shutil.copy(list[i], new_files)
                i += 1
        if choice == 5:
            file_name = input()
            fn_dupl = file_name + ".dupl"
            shutil.copy(file_name, fn_dupl)
        if choice == 6:
            change_dir = input()
            os.chdir(change_dir)
            data = os.listdir()
            for i in range(len(data)):
                if data[i].endswith(".dupl") is True:
                    os.remove(data[i])
                else:
                    continue
    elif quastion == "N":
        print("Мужик я тобою не доволен!")
    else:
        pass