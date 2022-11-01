def get_count_char(str_):
    dictionary = {}
    str_ = str_.lower()
    for symbol in str_:
        if symbol not in dictionary.keys():
            if symbol.isalpha():
                dictionary[symbol] = str_.count(symbol)
    return dictionary


def dict_percent(dictionary: dict, string_: str):
    count_symbols = len(string_)
    for symbol, count in dictionary.items():
        dictionary[symbol] = round((count / count_symbols) * 100, 2)
    return dictionary


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(dict_percent(get_count_char(main_str), main_str))
