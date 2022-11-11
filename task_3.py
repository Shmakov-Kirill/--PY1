import string
from random import sample
def get_random_password() -> str:
    password = ''
    length_ = 8
    all_symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = "".join(sample(all_symbols, length_))
    return password


print(get_random_password())
