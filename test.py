'''Задача 2 Normal'''
#calendar_data = input().replace('.', ' ').split()
#numbers_dict_day = {'01': 'первое', '02': 'второе', '03': 'третее', '04': 'четвёртое', '05': 'пятое'}
#numbers_dict_month = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая'}
#numbers_dict_year = {'2010': '2010 года', '2011': '2011 года', '2012': '2012 года', '2013': '2013 года', '2014': '2014 года'}
#print(numbers_dict_day[calendar_data[0]] + ' ' + numbers_dict_month[calendar_data[1]] + ' ' + numbers_dict_year[calendar_data[2]])
'''Задача 3 Normal'''
#from random import randint
#list_with_digits = []
#i = 0
#while i != 5:
    #list_with_digits.append(randint(-100, 100))
    #i += 1
'''Задача 4 Normal'''
#from collections import Counter
#lst = [1 , 2, 4, 5, 6, 2, 5, 2]
#lst_2 = []
#repetition_dict = Counter(lst)
#values = repetition_dict.values()
#values_lst = list(values)
#keys = repetition_dict.keys()
#keys_lst = list(keys)
#i = 0
#while i < len(values_lst):
    #if values_lst[i] == 1 :
        #lst_2.append(keys_lst[i])
    #i += 1
#print(lst_2)
'''Задача 1 Hard'''
import string
text = input()
sub_string_list = list(string.ascii_letters)
x = 0
for i in range(len(sub_string_list)):
    if sub_string_list[i] in text:
        a = text.count(sub_string_list[i])
        x += a
print(x)



