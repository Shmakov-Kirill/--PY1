def delete(list_, index=None):
    if index is not None:  # TODO реализовать функцию удаления элемента из списка по индексу
        slice_list_1 = list_[:index]
        slice_list_2 = list_[index + 1:]
        sum_list = slice_list_1 + slice_list_2
        return sum_list
    else:
        return list_[:-1]

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
