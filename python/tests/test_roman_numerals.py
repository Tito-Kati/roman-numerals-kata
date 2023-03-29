from src.roman_numerals import RomanNumerals


class TestRomanNumerals:

    def test_returns_I_when_1_given(self):
        roman_numerals = RomanNumerals()

        answer = roman_numerals.convert(1)

        assert answer == "I"
