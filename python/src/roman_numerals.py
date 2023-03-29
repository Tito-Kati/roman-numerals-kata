class RomanNumerals:

    equivalences = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    def convert(self, amount: int) -> str:
        if amount <= 0:
            raise Exception("amount must be greater than 0")

        if amount >= 4000:
            raise Exception("amount must be fewer than 4000")

        roman = ""
        rest = amount

        while rest > 0:
            for key in self.equivalences:
                if rest >= key:
                    rest -= key
                    roman += self.equivalences[key]
                    break

        return roman
