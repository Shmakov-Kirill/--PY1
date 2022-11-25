import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, "r") as f:
        table = []
        for line in f:
            words = line.rstrip("\n").split(',')
            table.append(words)
        headers = table[0]
        table = table[1:]

        dictionary_ = []
        for values in table:
            values = dictionary_.append(dict(zip(headers,values)))

        return dictionary_





print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
