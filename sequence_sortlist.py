from typing import List, Tuple

peoples_name[Tuple[str, int]] = [
    ("Philip", 56),
    ("Mary", 22),
    ("Mark", 52),
    ("Monica L", 36),
    ("Fridman", 41),
    ("Joe ", 66),
    ("Trump", 78),
    ("Winnie", 63),
    ("George ", 91),
]


def sort_by_age(arr: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    return sorted(arr, key=lambda person: person[1])


print(sort_by_age(famous_people))
