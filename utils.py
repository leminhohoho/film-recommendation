def empty_str_to_zero(v: str) -> int:
    if v == "":
        return 0
    return int(v)


def convert_to_list(string: str) -> list[int]:
    return list(map(empty_str_to_zero, string.split(",")))
