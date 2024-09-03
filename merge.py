om typing import Dict

buy_1: Dict[str, int] = {"gun": 1, "arrow": 3, "spear": 4}

buy_2: Dict[str, int] = {"arrow": 2, "shield": 1, "gun": 4}


def merge_dicts(dict_1: Dict[str, int], dict_2: Dict[str, int]) -> Dict[str, int]:
    merged = dict_1.copy()

    for key, value in dict_2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value

    return merged


print(merge_dicts(buy_1_, buy_2_))