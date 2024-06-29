import json


def get_data_transactions(path):
    """функция возвращает список словарей с данными о  транзакциях"""
    json_data_transaction = []
    try:
        with open(path, 'r', encoding="utf-8") as f:
            json_data_transaction = json.load(f)
            return json_data_transaction
    except json.JSONDecodeError:
        return json_data_transaction
    except FileNotFoundError:
        return json_data_transaction


if __name__ == "__main__":
    file_path = "..\\data\\operations.json"
    x = get_data_transactions(file_path)
    print(x)



