from datetime import datetime
import json


def get_operations_file():
    """
    Читает данные из файла operations.json
    :return: список транзакций
    """
    with open('operations.json', 'r', encoding='utf-8') as json_file:
        data = json.loads(json_file.read())
    return data


def get_filtr_list(data):
    """Фильтрует список транзакций по наличию ключа "state" и возвращает успешные операции

    """
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED' and x.get('date')]

    return data


def get_sort_list(data):
    """Сортирует 5 последних операций
    """
    data.sort(key=lambda x: datetime.strptime(x.get("date"), "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    return data[0:5]


def get_format_num(value):
    sender = value.split()
    formated_num = sender.pop(-1)
    cart_info = " ".join(sender)
    formated_num = f"{cart_info} {formated_num[:4]} {formated_num[4:6]}** **** {formated_num[-4:]}"

    return formated_num


def get_format_list(data):
    formatted_data = []
    for value in data:
        date = datetime.strptime(value['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = value['description']
        if "from" in value:
            from_arrow = "->"
            sender = mask_number(value['from'])
        else:
            sender = "Открытие счета"
            from_arrow = ":"
        sender_bill = value['to'].split()
        bill = sender_bill.pop(-1)
        if 'to' in value:
            bill = mask_number(value['to'])
        operation_sum = value['operationAmount']['amount']
        operation_currency = value['operationAmount']['currency']['name']
        formatted_data.append(f"""
        {date} {description}
        {sender} {from_arrow}  {bill}
        {operation_sum} {operation_currency}
                  """)

    return formatted_data


def mask_number(str_):
    """
    Маскирует номара карт в формате XXXX XX ** XXXX
    и счетов в формате XXXX
    :param str_: строка с указанием номера
    :return: строка с замаскированным номером
    """
    if "Maestro" in str_ or "MasterCard" in str_ or "Visa" in str_:
        card_number = str_.split()[-1]
        masked_card_number = f"{card_number[:4]} {card_number[4:6]}{'*' * 2} **** {card_number[-4:]}"
        new_str = str_.replace(card_number, masked_card_number)
# Маскирует номер счета, последнее слово в строке - это номер счета
    elif 'Счет' in str_:
        account_number = str_.split()[-1]
        masked_account_number = f"**{account_number[-4:]}"
        new_str = str_.replace(account_number, masked_account_number)
    else:
        new_str = str_
    return new_str
