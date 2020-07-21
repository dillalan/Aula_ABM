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
        """
        A cash addition to a a given entity's account
        :param cash: (int)
        """
        self.net += cash

    def draw_cash(self, cash):
        """
        Withdraw cash for a given account, and return the amount taken to the caller.
        :param cash: (int) a value to withdraw
        :return: (int) the withdrawn value
        """
        self.net -= cash
        return cash


if __name__ == '__main__':
    pass
