def card_number_hider(payment_number: int) -> str:
    """Функция для скрытия номера карты"""

    str_payment_number = str(payment_number)
    if len(str_payment_number) == 16:
        hidden_payment_number = f"{str_payment_number[0:4]} {str_payment_number[4:6]}** **** {str_payment_number[-4:]}"
        return hidden_payment_number
    else:
        return "Ошибка! Введите корректные данные"


def account_number_hider(account: int) -> str:
    """Функция для скрытия номера счёта"""

    str_account = str(account)
    if len(str_account) == 20:
        hidden_payment_account = "**" + str_account[-4:]
        return hidden_payment_account
    else:
        return "Ошибка! Введите корректные данные"


result = card_number_hider(7000792289606361)
result_1 = account_number_hider(73654108430135874305)
result_2 = card_number_hider(123)
print(result_1)
