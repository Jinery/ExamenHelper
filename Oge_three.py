#Проверка условия.
def valuate_condition(condition, x):
    return eval(condition)

#Максимумы.
#Выведет максимальное ложное логическому выражению.
def check_not_max(start_r: int, end_r: int, condition):
    a = 0
    for i in range(start_r, end_r, +1):
        if not valuate_condition(condition, i):
            a = i
    return a


condition = 'not(x < 6) or (x < 5)' #Сюда передайте логическое выражение.
result = check_not_max(1, 100, condition) #Передаём всё в функцию проверки. Первое число начало цикла, второе число конец цикла, третье пример.
print(result) #Выводим результат.

#Выведет максильное истинное логическому выражению.
def check_max(start_r: int, end_r: int, condition):
    a = 0
    for i in range(start_r, end_r, +1):
        if valuate_condition(condition, i):
            a = i
    return a

cond = 'x > 5 and not x > 6'
print(check_max(1, 100, cond))

#Минимумы.
#Выведет минимальное ложное логическому значению.
def check_not_min(start_r: int, end_r: int, condition):
    a = 0
    for i in range(start_r, end_r, +1):
        if not valuate_condition(condition, i):
            if a > i or a == 0:
                a = i
    return a

#Выведет минимальное истинное логическому выражению.
def check_min(start_r: int, end_r: int, condition):
    a = 0
    for i in range(start_r, end_r, +1):
        if valuate_condition(condition, i):
            if a > i or a == 0:
                a = i
    return a


cond = 'x > 5 and x <= 7'
print(check_min(1, 100, cond))
