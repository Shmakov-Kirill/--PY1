list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index_max = 0

for number in range(len(list_numbers)):
    if list_numbers[number] > list_numbers[index_max]:
        index_max = number
list_numbers[index_max], list_numbers[-1] = list_numbers[-1], list_numbers[index_max]
print(list_numbers)
