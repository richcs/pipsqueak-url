from uuid import uuid4
from gmpy2 import digits


def generate_short_id() -> str:
    num_str = str(uuid4().int)[:12]
    return digits(int(num_str), 62)


def write(filename: str, key: str, value: str):
    file = open(filename, "a")
    file.write(key + " " + value + "\n")
    file.close()


def get(filename: str) -> dict[str, str]:
    d = {}
    with open(filename) as file:
        for line in file:
            (key, val) = line.split()
            d[key] = val
    return d

