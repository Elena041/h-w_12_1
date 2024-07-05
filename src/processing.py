def filter_by_state(inform: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращающая список словарей с введенным ключамом"""

    new_list = []

    for data in inform:
        if data.get("state") == state:
            new_list.append(data)

    return new_list


def sort_by_date(info: list[dict], reverse_list: bool = True) -> list[dict]:
    """Функция возвращающая новый список, в котором исходные словари отсортированы по убыванию даты"""
    sorted_list = sorted(info, key=lambda item: item["date"], reverse=reverse_list)

    return sorted_list
