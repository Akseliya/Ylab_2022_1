def cache(func):
    """Функция-декоратор: кэширование результата выполнения функции func."""
    def wrapper(*args):
        nonlocal cache_result

        if args in cache_result:
            return cache_result[args]
        cache_result[args] = func(*args)
        return cache_result[args]

    cache_result = {}

    return wrapper


@cache
def multiplier(number: int):
    return number * 2
