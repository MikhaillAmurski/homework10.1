from . masks import account_number_hider, card_number_hider


def mask_account_card(info_account_card: str) -> str:
    """Функция для скрытия номера карты или счёта"""
    name_card = ""
    nun_card = ""
    for i in info_account_card:
        if i.isalpha() is True or i == " ":
            name_card = name_card + i
        elif i.isdigit():
            nun_card = nun_card + i
    if name_card == "Счет ":
        return f"{name_card + account_number_hider(int(nun_card))}"
    else:
        return f"{name_card + card_number_hider(int(nun_card))}"


def get_data(info_of_date: str) -> str:
    """Функция для преобразования даты"""
    return f"{info_of_date[8:10]}.{info_of_date[5:7]}.{info_of_date[0:4]}"
