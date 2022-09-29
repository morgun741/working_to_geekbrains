# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО prin
#def lucky_ticket(ticket_number):
    #return sum(map(int, str(ticket_number)[0:3])) == sum(map(int, str(ticket_number)[3:]))
#digit = lucky_ticket(123326)
#def febonachi_func(n, m):
    #a = [0, 1]
    #i = 0
    #hile i < m:
        #b = a[-1] + a[-2]
        #a.append(b)
        #i += 1
    #return print(a[n-1: m])
#a = febonachi_func(1, 20)


#Написать консольное меню вида:
#1. Добавить
#2. Удалить
#3. Распечатать
#4. Посчитать
#5. Выйти

#Надо чтобы
#а) Можно было удобно менять порядок меню и\или добавлять\удалять пункты меню
#б) Каждое действие (добавить, удалить и тд) должно быть функцией
#в) У пользователя надо спросить номер команды
#г) Программа не должна завершаться пока не введется команда Выйти
#д) Проверять на ввод ошибочных данных, там где они могут появиться


def print_menu(menu):
    for i, key in enumerate(menu, start=1):
        print(f"{i}. {key}")
def get_command(limit):
    command = int(input("Input command "))
    if 1 <= command <= limit:
        return command

def add():
    print("Add")
def delete():
    print("Delete")
def count():
    print("Count")
def show():
    print("Show")
def finish():
    exit()
menu ={
    "Add": add,  #функция тоже может выступать как пременная если её вставлять без указания скобок
    "Delete": delete,
    "Count": count,
    "Show": show,
    "Finish": finish
}
while True:
    print_menu(menu)
    command = get_command(len(menu))
    if command is not None:
        key = list(menu.keys())[command -1]
        menu[key]()
    else:
        print("wrong")