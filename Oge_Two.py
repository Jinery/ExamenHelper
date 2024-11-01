#Второе задание.
def decode_message(binary_message : str, code_to_letter):
    password = ''

    i = 0
    while i < len(binary_message):
        for length in [2, 3]:
            code = binary_message[i:i + length]
            if code in code_to_letter:
                password += code_to_letter[code]
                i += length
                break
        else:
            break

    return password


#Сюда Зашифрованное сообщение
binary_message = "0011000001110010"

#Сюда сопоставление букв с их цифрами из таблицы.
code_to_letter = {
    '11': 'А',
    '011': 'Г',
    '010': 'Л',
    '001': 'М',
    '000': 'Н',
    '10': 'О'
}

decoded_password = decode_message(binary_message, code_to_letter)

print(decoded_password)
