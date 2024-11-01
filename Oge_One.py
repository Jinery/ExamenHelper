#Первое задание.
def find_removed_element(text: str, encoding: str, elements, less_bytes: int):
    def get_size_in_bytes(s):
        return len(s.encode(encoding))

    original_size = get_size_in_bytes(text)

    for element in elements:
        new_text = text.replace(element + ', ', '').replace(element, '')
        new_size = get_size_in_bytes(new_text)

        if original_size - new_size == less_bytes:
            return element
    return None


#Исходный текст
text = "Бор, азот, гелий, натрий, водород, кислород, рентгений, менделевий, резерфордий – химические элементы"

#Добавляем список элементов.
elements = ["Бор", "азот", "гелий", "натрий", "водород", "кислород", "рентгений", "менделевий", "резерфордий"]

encoding = 'utf-16' #Кодировка.

#Вызываем функцию проверки элементов
removed_element = find_removed_element(text, encoding, elements, 18)

#Выводим результат.
print(removed_element)
