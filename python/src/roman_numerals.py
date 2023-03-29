class RomanNumerals:

    equivalences = {
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
    }

    def convert(self, amount: int) -> str:
        roman = ""
        rest = amount

        for _ in range(3):
            for key in self.equivalences:
                if rest >= key:
                    rest -= key
                    roman += self.equivalences[key]
                    break

        for _ in range(rest):
            roman += "I"

        return roman
