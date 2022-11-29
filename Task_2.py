import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename, "r") as f:
        table = []
        for line in f:
            table.append(line.rstrip(new_line).split(delimiter))
        headers = table[0]
        table = table[1:]

        dictionary_ = []
        for values in table:
            values = dictionary_.append(dict(zip(headers,values)))

        return dictionary_





print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
