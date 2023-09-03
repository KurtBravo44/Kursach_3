from utils.encoding_data import encoding_data

def test_encoding_data():
    assert encoding_data("Счет 78544755774551298747") == "Счет **8747"