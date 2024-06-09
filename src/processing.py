from src.widget import get_data


def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция фильтрации операций по ключу state"""
    new_list = []
    for i in list_dict:
        for key, value in i.items():
            if value == state:
                new_list.append(i)
    return new_list


def sort_by_date(list_dict: list, user_rev: bool = True) -> list:
    """Функция сортировки операций по дате"""
    if user_rev is True:
        sorted_list = sorted(list_dict, key=lambda x: get_data(x["date"]))
        return sorted_list
    else:
        sorted_list = sorted(list_dict, key=lambda x: get_data(x["date"]), reverse=False)
        return sorted_list
