# Ylab_2022_1

**Решение задач курса от Ylab.**

### Part 1
____
- `task_1_1` - найти домен url-адреса.
```
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
```
____
- `task_1_2` - привести 32-битное число к строковому виду IPv4.
```
assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"
```
____
- `task_1_3` - найти кол-во конечных нулей в факториале числа.
```
assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
```
____
- `task_1_4` - вернуть все возможные варианты составления слова `'banana'` из заданной строки.
```
assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
```
____
- `task_1_5` - найти все числа до заданного `limit`, состоящие из всех и только переданных простых множителей `primesL`. Вернуть их кол-во и максимальное из них.
```
primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
```
____

### Part 2

- `task_2_1` - написать циклический итератор `CyclicIterator`, итерируемый по переданному итерируемому объекту.

- `task_2_2` - реализовать метод `schedule` класса `Movie`, который будет генерировать дни, в которые показывают фильм.

- `task_3_1` - написать функцию-декоратор кэширования результата выполнения переданной функции.

- `task_3_2` - написать функцию-декоратор для многократного вызова переданной функции.

- `task_3_3` - сделать рефакторинг кода в соответствии с принципами SOLID.
