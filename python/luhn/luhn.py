class Luhn:
    def __init__(self, card_num):
        card_num = card_num.replace(" ", "")[::-1]
        self.validity = ((sum([((int(i)*2 if int(i)*2 < 10 else int(i)*2 - 9) if
                len(card_num[:idx])%2 != 0 else int(i)) for idx, i in
                enumerate(card_num)])) % 10 == 0 if
                card_num.isnumeric() and len(card_num) > 1 else
                False)


    def valid(self):
        return self.validity
