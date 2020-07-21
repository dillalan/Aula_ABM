# Sugiro que depois o random seja colocado lá na simulation.py e você já traga o número de cada loja
import random
from Exercise2.Conta import Conta


def pick_fantasy():
    """
    A function to assign a name to Store entities. The
    :return: (string) A name from fantasy_name.txt
    """
    my_name = open('fantasy_name.txt', encoding='utf-8')
    name = str()
    for name in range(random.randint(1, 54)):
        name = my_name.readline()
    return name


class Loja:
    """
    A store that sell goods/services. Stores have an ID, a product(which provide some experience), a capacity limit to
    assist their costumers, and an account(class) where the transactions are registered.
    """

    def __init__(self, reg):
        self.id = reg
        self.name = pick_fantasy()
        self.capacity = random.randint(10, 30)
        self.acc = Conta(0)
        self.cost_product = round(random.random() * 10, 2)
        self.experience = random.randint(0, 10)

    def sell_price(self):
        """
        A function that return price cost of the Store product
        :return: (float)
        """
        return self.cost_product

    def capacity_check(self):
        """
        Check if there is a clear spot for a new costumer
        :return: (Boolean)
        """
        if self.capacity >= 0:
            if self.capacity == 0:
                return False
            return True

    def update_experience(self):
        """
        A function that uptade the returned store experience according to the store capacity to receive clients.
        A more crowed store returns less experience that it initial preset.
        :return:
        """
        self.experience = round(self.experience * ((self.capacity - 1) / self.capacity), 1)

    def product(self):
        """
        A function that simulates a purchase of product, returning experience to the caller.
        :return: (float)
        """
        return self.experience

    def __repr__(self):
        return f'ID: {self.id} @ {self.name}'


if __name__ == '__main__':
    pass
