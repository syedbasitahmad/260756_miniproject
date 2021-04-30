from file_manage import count_characters
from file_manage import count_without_space
from file_manage import count_occurances


def test_count_characters():
    assert count_characters() == 3561


def test_count_without_space():
    assert count_without_space() == 3027


def test_count_occurances():
    assert count_occurances() == 5