from file_manage import count_characters, count_without_space, count_occurrences, count_words, append_text


def test_count_characters():
    assert count_characters() == 3561


def test_count_without_space():
    assert count_without_space() == 3027


def test_count_occurrences():
    assert count_occurrences() == 5


def test_count_words():
    assert count_words() == 550


def test_append_text():
    assert append_text() == 1
