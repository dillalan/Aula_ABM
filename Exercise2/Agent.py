from Exercise2.Conta import Conta
import random


def pick_name():
    my_name = open('name_list.txt', encoding='utf-8')
    name = str()
    for name in range(random.randint(1, 200)):
        name = my_name.readline()
    return name


class Agent:
    """
    An agent with name, age and an id. He(or she) have a bank account and a level of experience
    """

    def __init__(self, id):
        self.id = id
        self.name = pick_name()
        self.age = random.randint(15, 95)
        self.acc = Conta(0)
        self.exp = 0
        self.no_go = list()

    def __repr__(self):
        return f'{self.name} |Net Fund: {self.acc.net}| \n |Experience: {self.exp}|'

    def check_funds(self, loja):
        if self.acc.net >= loja.cost_product:  # como generalizar a loja???
            return True
        else:
            return False


if __name__ == '__main__':
    test = Agent(0)
    print(test)
