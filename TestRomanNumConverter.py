import pytest
from RomanNumConverter import rules, convert_numeral_to_num


# Define a fixture to set up common variables or objects needed for testing
@pytest.fixture
def valid_numerals():
    return {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


# Test case for checking if the rules function correctly identifies valid Roman numerals
def test_valid_numerals(valid_numerals):
    assert rules('IX', valid_numerals) is True
    assert rules('XXIV', valid_numerals) is True
    assert rules('MCMXCIV', valid_numerals) is True


# Test case for checking the conversion of Roman numerals to decimal numbers
def test_convert_numeral_to_num(valid_numerals):
    assert convert_numeral_to_num('IX', valid_numerals) == 9
    assert convert_numeral_to_num('XXIV', valid_numerals) == 24
    assert convert_numeral_to_num('MCMXCIV', valid_numerals) == 1994
    assert convert_numeral_to_num('MMMM', valid_numerals) == 4000
    assert convert_numeral_to_num('MMMMCMXCIX', valid_numerals) == 4999
    assert convert_numeral_to_num('MCMXC', valid_numerals) == 1990
    assert convert_numeral_to_num('DCCCXC', valid_numerals) == 890


