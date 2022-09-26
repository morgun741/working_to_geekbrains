# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО prin
#def lucky_ticket(ticket_number):
    #return sum(map(int, str(ticket_number)[0:3])) == sum(map(int, str(ticket_number)[3:]))
#digit = lucky_ticket(123326)
def febonachi_func(n, m):
    a = [0, 1]
    i = 0
    while i < m:
        b = a[-1] + a[-2]
        a.append(b)
        i += 1
    return print(a[n-1: m])
a = febonachi_func(1, 20)
