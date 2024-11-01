def evaluate_expression(example, b):
    example_with_value = example.replace('b', str(b))
    return eval(example_with_value)


def check_example(start_r: int, end_r: int, oper_r, example, equ_num):
    for b in range(start_r, end_r, oper_r):
        if evaluate_expression(example, b) == equ_num:
            return b

example = '(8+1+1)*b+1+1' #Пример.
equ_num = 62 #Значение, которому должно быть равно.
start_r = 1 #Начало цикла.
end_r = 10 #Конец цикла.
oper_r = +1 #Операция внутри цикла.

#При передаче примера не забывайте ставить скобки! Математика важна даже в программировании.
print(check_example(start_r, end_r, oper_r, example, equ_num))
