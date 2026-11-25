# 1.Создайте пустой словарь

# phone_book = {}


# 2. Реализуйте функции:
#
# add(name, phone) — добавить контакт.
#
# Если имя уже есть — обновить номер.
#
# Вывести сообщение о добавлении.

numbers = {
    'Maria': '555-01-03',
    'Alex': '344-12-88'
}


def add(name, phone):
    numbers[name] = phone
    print(f'Контакт {name} успешно добавлен')


add('Oleg', '555-07-04')
add('Ivan', '777-02-11')

print(numbers)


# find(name) — найти контакт по имени.
#
# Если найден — вывести имя и номер.
#
# Если нет — вывести сообщение «Контакт не найден».


def find(name):
    if name in numbers:
        print(f'Имя: {name}, номер: {numbers[name]}')
    else:
        print('Контакт не найден')


add('Dima', '555-07-04')

find('Maria')
find('Oleg')
find('Ivan')


# delete(name) — удалить контакт.
#
# Если удалён — вывести сообщение об удалении.
#
# Если нет — вывести «Контакт не найден».


def delete(name):
    if name in numbers:
        del numbers[name]
        print(f'Контакт {name} успешно удалён')
    else:
        print('Контакт не найден')


delete('Oleg')
print(numbers)


# list_all() — показать все контакты.
#
# Если книга пуста — вывести «Телефонная книга пуста».
#
# Иначе — вывести все контакты в формате Имя: Номер.


def list_all():
    if not numbers:
        print('Телефонная книга пуста')
    else:
        for name, phone in numbers.items():
            print(f'{name}: {phone}')


list_all()

# Сделайте меню с выбором действий (1 — добавить, 2 — найти, 3 — удалить, 4 — показать все, 5 — выход).
#
# Программа должна работать в цикле, пока пользователь не выберет выход.


while True:
    print('\n1 — Добавить контакт')
    print('2 — Найти контакт')
    print('3 — Удалить контакт')
    print('4 — Показать все контакты')
    print('5 — Выход')

    choice = input('Выберите действие: ')

    if choice == '1':
        name = input('Введите имя: ')
        phone = input('Введите номер: ')
        add(name, phone)

    elif choice == '2':
        name = input('Введите имя: ')
        find(name)

    elif choice == '3':
        name = input('Введите имя: ')
        delete(name)

    elif choice == '4':
        list_all()

    elif choice == '5':
        print('Выход из программы')
        break

    else:
        print('Неверный выбор!')
