from src.roman_numerals import RomanNumerals
import pytest

class TestRomanNumerals:

    numbers = [
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (9, "IX"),
        (10, "X"),
        (20, "XX"),
        (29, "XXIX"),
        (30, "XXX"),
        (35, "XXXV"),
        (40, "XL"),
        (50, "L"),
        (80, "LXXX"),
        (90, "XC"),
        (100, "C"),
        (294, "CCXCIV"),
        (400, "CD"),
        (500, "D"),
        (900, "CM"),
        (1000, "M"),
        (2019, "MMXIX"),
    ]

    @pytest.mark.parametrize("given,expected", numbers)
    def test_returns_conversion(self, given, expected):
        roman_numerals = RomanNumerals()

        answer = roman_numerals.convert(given)

        assert answer == expected

    def test_throws_error_when_number_is_less_than_0(self):
        roman_numerals = RomanNumerals()

        with pytest.raises(Exception) as error:
            roman_numerals.convert(0)

        assert str(error.value) == "amount must be greater than 0"

    def test_throws_error_when_number_is_more_than_4000(self):
        roman_numerals = RomanNumerals()

        with pytest.raises(Exception) as error:
            roman_numerals.convert(4000)

        assert str(error.value) == "amount must be fewer than 4000"
