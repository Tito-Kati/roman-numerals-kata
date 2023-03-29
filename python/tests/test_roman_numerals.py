from src.roman_numerals import RomanNumerals
import pytest

class TestRomanNumerals:

    numbers = [
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
    ]

    @pytest.mark.parametrize("given,expected", numbers)
    def test_returns_conversion(self, given, expected):
        roman_numerals = RomanNumerals()

        answer = roman_numerals.convert(given)

        assert answer == expected
