import re
from typing import Iterable, Iterator, Any, Set, List


def filter_query(value: str, data: Iterable[str]) -> Iterator[str]:
    """
    Функция фильтрации запроса (входных данных)
    """
    return filter(lambda x: value in x, data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> Set[str]:
    """
    Функция уникализации запроса
    """
    return set(data)


def limit_query(value: str, data: Iterable[str]) -> List[str]:
    """
    Функция установки лимита на вывод данных
    """
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value: str, data: Iterable[str]) -> Iterator[str]:
    """
    Функция деления исходных данных
    на колонки по пробелу
    """
    col_number = int(value)
    return map(lambda x: x.split(" ")[col_number], data)


def sorted_query(value: str, data: Iterable[str]) -> List[str]:
    """
    Функция сортировки данных по возрастанию
    или убыванию
    """
    reverse = value == "desc"
    return sorted(data, reverse=reverse)


def reqex_query(value: str, data: Iterable[str]) -> Iterator[str]:
    """
    Функция чтения регулярных выражений
    """
    pattern = re.compile(value)
    return filter(lambda x: re.search(pattern, x), data)
