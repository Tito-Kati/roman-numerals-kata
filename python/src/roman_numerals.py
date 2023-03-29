class RomanNumerals:

    equivalences = {
        10: "X",
        5: "V",
        4: "IV",
    }

    def convert(self, amount: int) -> str:
        for key in self.equivalences:
            if amount == key:
                return self.equivalences[key]

        roman = ""
        for _ in range(amount):
            roman += "I"
        return roman
