from random import randint
def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(list_) < 16:
        random_symbol = randint(-10, 10)
        if random_symbol not in list_:
            list_.append(random_symbol)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
