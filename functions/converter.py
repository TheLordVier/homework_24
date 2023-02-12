from typing import Dict, Callable, Optional, Iterable, List

from functions.queries_functions import filter_query, unique_query, limit_query, map_query, sorted_query, reqex_query


CMD_TO_FUNCTIONS: Dict[str, Callable] = {
    "filter": filter_query,
    "unique": unique_query,
    "limit": limit_query,
    "map": map_query,
    "sort": sorted_query,
    "regex": reqex_query
}


def read_file(file_name: str) -> Iterable[str]:
    """
    Функция чтения исходного файла
    """
    with open(file_name) as file:
        for line in file:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> List[str]:
    """
    Функция для построения запроса
    """
    if data is None:
        prepared_data: Iterable[str] = read_file(file_name)
    else:
        prepared_data = data

    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepared_data))
