'''
Напишите функцию, которая получает на вход массив строк и удаляет из него все строки, в которых нет как минимум двух букв русского алфавита. Две одинаковые буквы тоже считаются: например, функция не должна удалять строку «бб».
'''

def save_ru(strings: list):
    s_index = 0
    ru_letters = "йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЁЯЧСМИТЬБЮ"
    while(s_index < len(strings)):
        flag = 0
        for letter in strings[s_index]:
            if letter in ru_letters:
                flag += 1
                if flag == 2:
                    break
        if flag < 2:
            strings.pop(s_index)
            continue
        s_index += 1

test_cases = ["фккка", "qwer", "123", "", "ба", "1er", "qq", "бб", "wwq", "МФАЫВЫ" ]
print("input:", test_cases)
save_ru(test_cases)
print("output:", test_cases)
