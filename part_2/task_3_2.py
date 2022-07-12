import time


def multiple_call(call_count: int, start_sleep_time: int, factor: int, border_sleep_time: int):
    """Функция-декоратор: многократный вызов функции func.

    :param call_count: кол-во вызовов функции func
    :param start_sleep_time: начальное время ожидания (сек)
    :param factor: во сколько раз будет увеличиваться время ожидания перед следующим вызовом
    :param border_sleep_time: максимальное время ожидания (сек)
    """
    def decorator(func):
        def wrapper(*args):
            sleep_time = start_sleep_time
            for iter_num in range(call_count):
                time.sleep(sleep_time)
                result = func(*args)
                print(f'Запуск номер {iter_num + 1}. Ожидание: {sleep_time} секунд. Результат декорируемой функции = '
                      f'{result}.')
                sleep_time *= factor
                if sleep_time > border_sleep_time:
                    sleep_time = border_sleep_time

        return wrapper

    return decorator
