# Sugiro que depois o random seja colocado lá na simulation.py e você já traga o número de cada loja
import random
from Exercise2.Conta import Conta


def pick_fantasy():
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
        self.acc = Conta(0)
        self.cost_product = round(random.random() * 10, 2)
        self.experience = random.randint(0, 10)
        self.capacity = random.randint(5, 200)

    def sell_price(self):
        return self.cost_product

    def capacity_check(self):
        if self.capacity >= 0:
            if self.capacity == 0:
                return False
            return True

    def product(self):
        return self.experience

    # TODO: altera a experiencia de acordo com a capacidade

    def __repr__(self):
        return f'ID: {self.id} @ {self.name}'


if __name__ == '__main__':
    pass
