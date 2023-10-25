class EmptyArgsError(Exception):
    pass


class NoResultError(Exception):
    pass


def drink_in_hot_day(*args, temp=5):
    if len(args) == 0:
        raise EmptyArgsError("No arguments")
    very_useful_list = []
    for i in args:
        if not isinstance(i, str):
            raise TypeError("Not all strings")
        if len(i) > temp:
            very_useful_list.append(i)
    if len(very_useful_list) == 0:
        raise NoResultError("Empty list")
    return sorted(very_useful_list, key=lambda x: (len(x), x))
