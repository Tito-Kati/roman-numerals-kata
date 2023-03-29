from src.roman_numerals import RomanNumerals


class TestRomanNumerals:

    def test_returns_I_when_1_given(self):
        roman_numerals = RomanNumerals()

        answer = roman_numerals.convert(1)

        assert answer == "I"

    def test_returns_II_when_2_given(self):
        roman_numerals = RomanNumerals()

        answer = roman_numerals.convert(2)

        assert answer == "II"

    def test_returns_III_when_3_given(self):
        roman_numerals = RomanNumerals()

        answer = roman_numerals.convert(3)

        assert answer == "III"
