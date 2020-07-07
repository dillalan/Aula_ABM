class Conta:

    def __init__(self, cc):
        """
        :param cc: an identifier. Type int.
        """
        self.id = cc
        self.net = 0

    def __repr__(self):
        return f'Account: {self.id} @ Net Fund $ {self.net}'

    def deposit(self, cash):
        self.net += cash

    def draw_cash(self, cash):
        self.net -= cash
        return cash


if __name__ == '__main__':
    pass
