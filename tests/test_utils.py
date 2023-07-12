
from utils import get_operations_file, get_filtr_list, get_sort_list, get_format_num, get_format_list, mask_number


def test_get_operations_file():
    assert isinstance(get_operations_file(), list)


def test_get_filtr_list():
    assert len([{"state": "EXECUTED"}]) == 1


def test_get_sort_list():
    test_data = [
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {
                "amount": "51463.70",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 48894435694657014368",
            "to": "Счет 38976430693692818358"
        },
        {
            "id": 490100847,
            "state": "EXECUTED",
            "date": "2018-12-22T02:02:49.564873",
            "operationAmount": {
                "amount": "56516.63",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 8326537236216459",
            "to": "MasterCard 6783917276771847"
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215"
        },
    ]
    sorted_data = get_sort_list(test_data)
    assert [x['date'] for x in sorted_data] == ['2019-07-12T20:41:47.882230', '2018-12-22T02:02:49.564873',
                                                '2018-07-11T02:26:18.671407']


def test_get_format_list():
    test_data = [
        {
            "id": 154927927,
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614",
            "operationAmount": {
                "amount": "30153.72",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 7810846596785568",
            "to": "Счет 43241152692663622869"
        }

    ]
    format_data = get_format_list(test_data)
    assert format_data() == [
        "\n19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 ->  Счет **2869\n30153.72 руб.\n          "
    ]


def test_mask_number():
    assert mask_number([{"from": "Maestro 7810846596785568",}]) == [{"from": "Maestro 78** **** 9678 5568"}]
