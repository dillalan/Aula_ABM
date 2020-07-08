import random
from Exercise2.Loja import Loja
from Exercise2.Agent import Agent


class Simulacao:
    def __init__(self):
        self.stores = list()
        self.customers = list()
        self.grow_stores()
        self.grow_customers()
        self.initial_cash()

    def txt_data(self):
        # TODO: Create a .txt with the run results
        # with open('arquivo1.csv', 'w') as handler as f:
        pass

    def grow_stores(self):
        """
        Generate stores. Type Loja
        :return: (list) of stores
        """
        for id in range(10):
            self.stores.append(Loja(id))

    def grow_customers(self):
        """
        Generate costumers. Type Agent
        :return: (list) of costumers
        """
        for id in range(10):
            self.customers.append(Agent(id))

    def mean_exp(self):
        """
        Takes the experience of all customers in given step
        :return: (float) the mean experience
        """
        exp_sum = 0
        for client in self.customers:
            exp_sum += client.exp
        return exp_sum / len(self.customers)

    def initial_cash(self):
        """
        A one time deposit to all costumers account. Represents the money they hold to spend in some store
        :return: (int) place value into costumers account
        """
        for client in self.customers:
            client.acc.deposit(random.randint(10, 20))

    def to_other_place(self, except_this, client):
        self.stores.remove(except_this)
        all_the_rest = random.choice(self.stores)
        print(self.stores)
        self.shopping(all_the_rest, client)

    def shopping(self, selected_store, client):
        # Check if its possible to enter the selected store
        its_a_go = selected_store.capacity_check()
        if its_a_go:
            # If its_a_go is True, check if the client have funds to buy the goods from the selected store
            if client.check_funds(selected_store):
                # If the costumer have funds, enters in the store lowering its capacity
                selected_store.capacity -= 1
                selected_store.acc.deposit(client.acc.draw_cash(selected_store.cost_product))
                # Buying some good from the store means that the store receive a deposit equivalent to the
                # value of the store product cost. This sum is removed from the costumer account
                client.exp += selected_store.product()
                # To buy a good it's to get an experience. This experience value its placed within costumer
                # attribute Agent.exp
                stay = client.exp > 5
                # Once it bought something the costumer decides to stay according to the gathered experience
                if not stay:
                    # If the costumer choose to leave, it clears space to a new costumer
                    selected_store.capacity += 1
                    # função pra escolher outra loja menos essa e recurse essa função
                    self.to_other_place(selected_store, client)
                else:
                    pass

    def run_model(self):
        # To every costumer on the list of costumers
        for client in self.customers:
            # Select a random store
            selected_store = random.choice(self.stores)
            self.shopping(selected_store, client)
        return self.mean_exp()


if __name__ == '__main__':
    minha_sim = Simulacao()
    media = minha_sim.run_model()
    print(media)
