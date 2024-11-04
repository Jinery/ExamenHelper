#13 задание.
import os


def find_and_get(rootdir: str, file_end: str):
    n = 0
    for subdir, dirs, files in os.walk(rootdir): #Перебираем все каталоги, подкаталоги, и файлы внутри указанного пути.
        for file in files: #Получив с цикла файлы проверяем все файлы.
            if file.endswith(file_end):
                #При нахождении файла с нужным расширением программа добавит 1.
                n += 1
    return n


rootdir = r'' #Путь до каталога.
file_end = '.htm' #Окончание файла.

print(find_and_get(rootdir, file_end))


def find_and_calculate(rootdir: str, file_end: str, operation, end_num: int):
    n = 0
    for subdir, dirs, files in os.walk(rootdir): #Перебираем все каталоги, подкаталоги, и файлы внутри указанного путиc.
        for file in files: #Получив с цикла файлы проверяем их.
            if file.endswith(file_end):
                file_path = os.path.join(subdir, file) #Регистрируем путь до файла.
                if operation(os.path.getsize(file_path), end_num): #Тут мы сразу получаем вес файла в байтах, и проводим операцию над ним и заданным объёмом.
                    n += 1
    return n #Возвращаем n, который указывает на кол-во файлов в каталоге, которые выдают истину при выполнении условия.

rootdr = r'' #Путь до каталога.
end_file = '.rtf' #Окончание файла.
operation = lambda x, y: x > y
end_num = 100000 #Объём считается в байтах! 1 килобайт - 1000 байт!

print(find_and_calculate(rootdr, end_file, operation, end_num))
