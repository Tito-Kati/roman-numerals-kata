class RomanNumerals:

    def convert(self, amount: int) -> str:
        roman = ""
        for _ in range(amount):
            roman += "I"
        return roman
