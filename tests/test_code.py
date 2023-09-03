import pytest
from utils.encoding_data import encoding_data
from utils.func import sort_file
from utils.func import output_of_operations
def test_encoding_data():
    assert encoding_data("Счет 78544755774551298747") == "Счет **8747"
    assert encoding_data("МИР 8193813157568899") == "МИР 819381******8899"
    assert encoding_data("Visa Gold 7756673469642839") == "Visa Gold 775667******2839"

    with pytest.raises(IndexError):
        encoding_data("123")




file_for_test = [
  {'id': 1, 'date': 3},
  {'id': 2, 'date': 2},
  {'id': 3, 'date': 1}
]
def test_sort_file():
  assert sort_file(file_for_test, 'date') == [
  {'id': 1, "date": 3},
  {'id': 2, "date": 2},
  {'id': 3, "date": 1}
]

  assert sort_file(file_for_test, 'id') == [
  {'id': 3, 'date': 1},
  {'id': 2, 'date': 2},
  {'id': 1, 'date': 3}
]



file_for_test_2 = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]

def test_output_of_operations():
    assert output_of_operations(file_for_test_2, 0) == (f"2019.08.26 Перевод организации\n"
 f"Maestro 159683******5199 --> Счет **9589\n"
 f"31957.58 руб.")
