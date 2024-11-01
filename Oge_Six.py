#6 задание.
def evalueate_condition(condition, s, k):
    condition_with_values = condition.replace('s', str(s)).replace('k', str(k))
    return eval(condition_with_values)


def check_nums(condition, cases, conc: str):
    n = 0
    for s, k in cases:
        if evalueate_condition(condition, s, k) and conc.lower() == "yes":
            n += 1
        elif not evalueate_condition(condition, s, k) and conc.lower() == "no":
            n += 1
    return n



#Список значений из условия.
test_cases = [
    (0, 2),
    (-1, 0),
    (2, 3),
    (4, 2),
    (3, 1),
    (-2, 7),
    (10, -2),
    (5, 4),
    (-7, 11)
]

print(check_nums('(s < 4) and not (k < 2)', test_cases, "YES")) #Вывод с вызовом функции. В первых кавычках логическое выражение, следом передаётся таблица...
#И напоследок вывод: "YES/NO", программа сама переведёт вывод в нужный регистр и выведет ответ!


#V2. Подставновка A.
def eval_cond(cond, s, t, A):
    cond_with_vals = cond.replace('s', str(s)).replace('t', str(t)).replace('A', str(A))
    return eval(cond_with_vals)


def check_and_set_nums(cond, cases, conc: str, r: int, eql_num: int):
    n = 0
    lost_a = -1
    for a in range(r):
        for s, k in cases:
            condition_met = eval_cond(cond, s, k, a)
            if (condition_met and conc.lower() == "yes") or (not condition_met and conc.lower() == "no"):
                if lost_a == a:
                    n += 1
                else:
                    lost_a = a
                    n = 1

                if n == eql_num:
                    return a

    return None


casses = [
    (1, 2),
    (11, 2),
    (1, 12),
    (11, 12),
    (-11, -12),
    (-12, 11),
    (10, 10),
    (10, 5)
]

cond = '(s > 10) or (t > A)' #Выражение.

print(check_and_set_nums(cond, casses, "NO", 12, 3))  #Передаём выражение, после него массив с числами, потом указываем что нам нужно, YES или NO, дальше указываем число для range. Последним аргументом передаём число, которое должно быть...
#Равно n.

#10 можно решить очень просто не писав никакие программы, и почти что не включая мозг.
'''Вы просто можете сделат в консоли python следующее: int('Число', Система счисления). Обязательно число указывайте как string-значение, а систему счисления как int(целочисленное) значение, и вы получите ответ ничего не перемножая и не считая...
...Если конечно условие не требует посчитать наибольшее число, но для этого тоже есть калькулятор в консоли Python. :)'''





