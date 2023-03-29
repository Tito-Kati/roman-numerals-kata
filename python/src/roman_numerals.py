class RomanNumerals:

    equivalences = {
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    def convert(self, amount: int) -> str:
        roman = ""
        rest = amount

        while rest > 0:
            for key in self.equivalences:
                if rest >= key:
                    rest -= key
                    roman += self.equivalences[key]
                    break

        return roman
