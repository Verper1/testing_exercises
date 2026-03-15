NOT_SET = "NOT_SET"


def first(items: list[int], default: int | None | str = NOT_SET) -> int | None:  # type: ignore
    # error: Incompatible return value type (got "int | str | None", expected "int | None")  [return-value]
    """Функция, которая возвращает первый элемент списка, иначе либо возвращает AttributeError, либо то, что было отдано в аргумент default"""
    if items:
        return items[0]
    if default == NOT_SET:
        raise AttributeError
    return default
