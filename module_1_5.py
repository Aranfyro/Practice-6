# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"

# Задание переменных различных типов данных:
immutable_var = 'Hello', 88, True, [1, 2]
print (immutable_var)

# Изменение значений переменных:
# immutable_var [0] = 'Bye
# immutable_var [1] = 00
# immutable_var [2] = False
#i mmutable_var [3] = [2, 3]
# Во всех случаях выше, я попытался изменить элементы кортежа, но выходила ошибка, это случалось потому,
# что кортеж не поддерживает обращение по элементам.
# Но можно изменить элементы самого элемента-списка внутри кортежа:
immutable_var [3] [:] = [0, 0]
print (immutable_var)

# Создание изменяемых структур данных:
mutable_list = ['Hello', 88, True, [1, 2]]
print ('Изначальный список: ', mutable_list)
mutable_list [0] = 'Bye'
mutable_list [1] = 00
mutable_list [2] = False
mutable_list [3] = [2, 3]
print ('Измененный список: ', mutable_list)