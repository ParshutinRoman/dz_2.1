from pprint import pprint
path = "/Users/admin/Desktop/netology/PY/dz_2.1"


with open('dishes_list.txt', 'r', encoding='utf8') as menu:

    dishes = {}
    quantity = []
    ingridients = []
    cook_book = {}

    for line in menu:
        dish = line.strip()
        dishes[dish] = [{}]
        q = int(menu.readline())
        quantity.append(q)
        dish_list = []
        for i in range(q):
            ingridient = menu.readline()
            ingridient = ingridient.strip()
            ingridient = ingridient.split('|')
            ingridients.append(ingridient)
            dish_list_item = {'ingridient_name': ingridient[0], 'quantity': int(ingridient[1]), 'measure': ingridient[2]}
            dish_list.append(dish_list_item)
            cook_book[dish] = dish_list
        menu.readline()

pprint(cook_book)





def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],\
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

print(cook_book)
create_shop_list()