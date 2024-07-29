import pytest
from string_utilits import StringUtils

utils = StringUtils()


# capitilize
@pytest.mark.parametrize("string_input, expected_string", [
    ("lada", "Lada"),
    ("привет", "Привет"),
    ("hello friends", "Hello friends"),
    ("123test", "123test"),
    ("test123", "Test123"),
    ("123", "123"),
    ("", ""),
    (" ", " ")
])
def test_capitilize(string_input, expected_string):
    utils = StringUtils()
    assert utils.capitilize(string_input) == expected_string


# trim
@pytest.mark.parametrize("string_input, expected_string", [
    ("  Lada", "Lada"),
    (" 123", "123"),
    (" Hello ", "Hello ")
])
def test_trim(string_input, expected_string):
    utils = StringUtils()
    assert utils.trim(string_input) == expected_string


@pytest.mark.xfail()
def test_trim_utils_with_numbers():
    assert utils.trim(123456) == "123456"


# to_list
@pytest.mark.parametrize("string, delimeter, result", [
    ("1,2,3", ",", ["1", "2", "3"]),
    ("red,blue,green", ",", ["red", "blue", "green"]),
    ("", None, []),
    ("вишня:малина:клубника", ":", ["вишня", "малина", "клубника"]),
    ("a,b,c,d", None, ["a", "b", "c", "d"])
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


# contains
@pytest.mark.parametrize("string_input, symbol, result", [
    ("Test", "s", True),
    ("123456", "5", True),
    ("Hello friend", " ", True),
    ("Анна-Мария", "-", True),
    ("", "", True),
    ("apple", "n", False),
    ("123456", "k", False),
    ("", "o", False),
    ("собака", "Л", False),
    ("dog", "", False)
])
def test_contains(string_input, symbol, result):
    res = utils.contains(string_input, symbol)
    assert res == result


# delete symbol
@pytest.mark.parametrize("string, symbol, result", [
    ("red", "e", "rd"),
    ("DogCat", "Cat", "Dog"),
    ("1234", "4", "123"),
    ("Hello World", " ", "HelloWorld"),
    ("кошка", "у", "кошка"),
    ("дом", "", "дом"),
    ("", "д", ""),
    ("", "", "")
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


# starts_with
@pytest.mark.parametrize("string, symbol, result", [
    ("Hello", "H", True),
    ("Good morning", "Good", True),
    ("123456", "1", True),
    (" Lada", " ", True),
    ("", "", True),
    ("Test", "K", False),
    ("123456", "5", False),
    (" Dog", "D", False),
    ("", "p", False)
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


# end_with
@pytest.mark.parametrize("string, symbol, result", [
    ("Hello", "o", True),
    ("Good morning", "morning", True),
    ("123456", "6", True),
    ("Lada ", " ", True),
    ("", "", True),
    ("Test", "l", False),
    ("123456", "5", False),
    ("Dog ", "g", False),
    ("", "p", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


# is_empty
@pytest.mark.parametrize("string, result", [
    ("", True),
    ("  ", True),
    ("   ", True),
    ("Hello", False),
    ("  Test", False),
    ("123456", False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


# list_to_string
@pytest.mark.parametrize("lst, joiner, result", [
    (["1", "2", "3"], ",", "1,2,3"),
    (["orange", "yellow", "black"], ", ", "orange, yellow, black"),
    (["Анна", "Мария"], "-", "Анна-Мария"),
    (["Tom", "Jerry"], " and ", "Tom and Jerry"),
    ([], None, ""),
    ([], ";", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner is None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result
