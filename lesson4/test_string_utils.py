from string_utils import StringUtils
import pytest


# тест функции capitilize
@pytest.mark.parametrize(
    'str, result',
    [("test", "Test"), ("Test", "Test"), ("1est", "1est"), (" test", " test"),
     ("test test test", "Test test test"), ("", "")])
def test_capitilize(str, result):
    string = StringUtils()
    res = string.capitilize(str)
    assert res == result


# тест функции trim
@pytest.mark.parametrize(
    'str, result',
    [(" test", "test"), ("Test", "Test"), ("  1est", "1est"),
     (" test ", "test "), ("    ", ""), ("", "")])
def test_trim(str, result):
    string = StringUtils()
    res = string.trim(str)
    assert res == result


# тест функции to_list
@pytest.mark.parametrize(
    'str, delimeter, result',
    [("a.b.c", ".", ["a", "b", "c"]), ("a,b,c", "a,b,c",["",""]),
     ("abc", ",", ["abc"]), ("a,,b", ",", ["a", "", "b"]),
     ("a,  ,b", ",", ["a", "  ", "b"]), ("", ",", [""])])
def test_to_list(str, delimeter, result):
    string = StringUtils()
    res = string.to_list(str, delimeter)
    assert res == result


# тест функции contains
@pytest.mark.parametrize(
    'str, symb, result',
    [("Test", "T", True), ("", "T", False), ("test", "T", False),
     ("Test", "P", False), ("Te1st", "1", True), ("Te st", " ", True),
     ("^^", "^", True)])
def test_contains(str, symb, result):
    string = StringUtils()
    res = string.contains(str, symb)
    assert res == result


# тест функции delete_symbol
@pytest.mark.parametrize(
    'str, del_symb, result',
    [("Test", "T", "est"), ("Tester", "e", "Tstr"), ("test", "T", "test"),
     ("Test", "Test", ""), ("Test", "TestTest", "Test")])
def test_delete_symbol(str, del_symb, result):
    string = StringUtils()
    res = string.delete_symbol(str, del_symb)
    assert res == result


# тест функции starts_with
@pytest.mark.parametrize(
    'str, symbol, result',
    [("Test", "T", True), ("Tester", "e", False), ("test", "T", False),
     (" Test", " ", True), ("T", "T", True), ("","", True)])
def test_starts_with(str, symbol, result):
    string = StringUtils()
    res = string.starts_with(str, symbol)
    assert res == result


# тест функции end_with
@pytest.mark.parametrize(
    'str, symbol, result',
    [("Test", "t", True), ("Tester", "e", False), ("test", "T", False),
     ("Test ", " ", True), ("T", "T", True), ("","", True)])
def test_end_with(str, symbol, result):
    string = StringUtils()
    res = string.end_with(str, symbol)
    assert res == result


# тест функции is_empty
@pytest.mark.parametrize(
    'str, result',
    [("", True), ("Tester", False), (" ", True), ("  ", True), ("  T", False)])
def test_is_empty(str, result):
    string = StringUtils()
    res = string.is_empty(str)
    assert res == result


# тест функции list_to_string
@pytest.mark.parametrize(
    'lst, joiner, result',
    [(["a", "b", "c"], ", ", "a, b, c"), ([1, "b", "c"], ", ", "1, b, c"),
     (["", ""], ", ", ", "), (["a", "b", "c"], " ", "a b c"),
     ([], ", ", ""), (["Test"], ", ", "Test"), ([""], ", ", "")])
def test_list_to_string(lst, joiner, result):
    string = StringUtils()
    res = string.list_to_string(lst, joiner)
    assert res == result
