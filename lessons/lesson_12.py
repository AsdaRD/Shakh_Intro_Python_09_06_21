# функции сортировки

# my_list = [12, 3, 45, 23, -10, 1]
#
# sorted_list = sorted(my_list, reverse=True, key=abs)
# print(sorted_list)


# def sort_by_len_and_name(name):
#     return len(name), name


# my_str_list = ['John', 'Jack', 'Jacob', 'Max', 'Chris', 'Kate']

# sort_str_list = sorted(my_str_list)  # по алфавиту
# print(sort_str_list)

# sort_str_list = sorted(my_str_list, key=len)  # по длине
# print(sort_str_list)

# sort_str_list = sorted(my_str_list, key=sort_by_len_and_name)  # по длине
# print(sort_str_list)

# def sort_by_price(price_dict):
#     price = price_dict['price']
#     name = price_dict['name']
#     return price, name


# price_list = [{'product': 'milk', 'price': 23},
#               {'product': 'ice-cream', 'price': 18},
#               {'product': 'meat', 'price': 120},
#               {'product': 'Pepsi-Cola', 'price': 10},
#               {'product': 'Coca-Cola', 'price': 10}
#               ]

# sorted_price_list = sorted(price_list, key=sort_by_price)
# print(sorted_price_list)

# регулярные выражения
import re

my_string = 'hjkdfhbdbnm,ljdsg 127.0.0.1 rtyujkl;,lmm yuikjbvnmsdlagn 200.23.12.201:5400 uwieajktkds z'

# template = r'\d+' # просто числовые группы
# template = r'[0-9a-zA-ZА-Я]+' #любой символ из данных 
template = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

result = re.findall(template, my_string)
print(result)