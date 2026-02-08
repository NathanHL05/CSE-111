"""Verify that the prefix and suffix functions work correctly."""

from words import get_prefix, get_suffix
import pytest


def test_get_prefix():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the prefix function and verify that it returns a string.
    pre = get_prefix("upbeat", "upgrade")
    assert isinstance(pre, str), "prefix function must return a string"

    # Call the prefix function ten times and use an assert
    # statement to verify that the string returned by the
    # prefix function is correct each time.
    assert get_prefix("cat", "catalog") == "cat"
    assert get_prefix("", "") == ""
    assert get_prefix("", "correct") == ""
    assert get_prefix("clear", "") == ""
    assert get_prefix("happy", "funny") == ""
    assert get_prefix("dogmatic", "dog") == "dog"
    assert get_prefix("jump", "joyous") == "j"
    assert get_prefix("upbeat", "upgrade") == "up"
    assert get_prefix("Disable", "dIstasteful") == "dis"

def test_get_suffix():

    suf1_list=["","","clear","angelic","found"]
    suf2_list=["","correct","","awesome","profound"]
    suf_return=["","","","","found"]

    for x in range(len(suf1_list)):
        word1= suf1_list[x]
        word2= suf2_list[x]
        actual= get_suffix(word1, word2)
        expected = suf_return[x]
        assert isinstance(actual, str)
        assert actual == expected






# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
