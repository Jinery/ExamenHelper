#10 задание.
def check_nums(nums, operation):
    a = 0
    old_num = 0
    for n, t in nums.items():
        num = int(n, t)
        if operation(old_num, num):
            old_num = num
    return old_num


nums = {
    '3E': 16,
    '44': 8,
    '1011110': 2
}

print(check_nums(nums, lambda x, y: x < y))


#Бывает такое что встречаются математические выражения со степенями, это мне самому попалось.
def check_and_sol(nums, operation):
    first_num, second_num = map(lambda n_t: int(n_t[0], n_t[1]), zip(nums.keys(), nums.values()))
    return operation(first_num, second_num)

#Этот код будет наверняка сложен многим. Так вот. Создаём две переменные, first_num, second_num, присваиваем им значения с помощью map и lambda...
#Переводим каждое число в нужную систему счисления, переводим их из словаря в тип ключ: значение. Возвращаем операцию над ними.


numbers = {
    '1011110': 2,
    '3E': 16
}

#Передаём таблицу с числами и системой счисления из условия задачи, добавляем лямбда-выражение чтобы указать что нужно сделать с ними(Прибавить, вычесть и т.д).
print(check_and_sol(numbers, lambda x, y: x - y))
