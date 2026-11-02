# Задача: Поиск дубликатов в списке (Python)
#
# Дан список чисел. Необходимо найти все элементы,
# которые встречаются в списке более одного раза.


number = [1, 2, 5, 7, 14, 1, 5]

duplicates=[]

for num in number:
    # Если число встречается >1 раза и его еще нет в duplicates
    # num not in duplicates — защита от повторного добавления
    if number.count(num)>1 and num not in duplicates:
        duplicates.append(num)  # добавляем дубликат

print(duplicates)
