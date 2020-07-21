import random
import csv
from Exercise2.Loja import Loja
from Exercise2.Agent import Agent


def to_data(data):
    with open('arquivo1.csv', 'w', newline='') as csvfile:
        handler = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
        handler.writerow(data)
        csvfile.close()


class Simulacao:
    def __init__(self):
        self.stores = list()
        self.customers = list()
        self.grow_stores()
        self.grow_customers()
        self.initial_cash()

    def grow_stores(self, n_stores=30):
        """
        Generate stores. Type Loja
        :return: (list) of stores
        """
        for id in range(n_stores):
            self.stores.append(Loja(id))

    def grow_customers(self, n_agents=100):
        """
        Generate costumers. Type Agent
        :return: (list) of costumers
        """
        for id in range(n_agents):
            self.customers.append(Agent(id))

    def mean_exp(self):
        """
        Takes the mean experience of all customers in given run
        :return: (float) the mean experience
        """
        exp_sum = 0
        for client in self.customers:
            exp_sum += client.exp
        return exp_sum / len(self.customers)

    def mean_acc(self, customer=True):
        """
        Takes the mean net fund of all customers in given run.
        Return customer mean net fund by default. customer = False return stores mean net fund by default
        :return: (float) the mean net fund
        """
        if customer:
            acc_sum = 0
            for client in self.customers:
                acc_sum += client.acc.net
            return acc_sum / len(self.customers)
        else:
            acc_sum = 0
            for store in self.stores:
                acc_sum += store.acc.net
            return acc_sum / len(self.stores)

    def mean_price(self):
        """
        Takes the mean price of all stores in a given run
        :return: (float) the mean price
        """
        price_sum = 0
        for store in self.stores:
            price_sum += store.cost_product
        return price_sum / len(self.stores)

    def initial_cash(self):
        """
        A one time deposit to all costumers account. Represents the money they hold to spend in some store
        :return: (int) place value into costumers account
        """
        for client in self.customers:
            client.acc.deposit(random.randint(10, 20))

    def to_other_place(self, except_this, client):
        """
        A function that eliminates a store, from his possible choices, where the agent was
        unsatisfied with the gained experience. Then calls the client to go shopping again.
        :param except_this: the bad store
        :param client: the client
        :return:
        """
        # Add a store in a list of no going back
        client.no_go.append(except_this)
        now_this = random.choice(self.stores)
        # Chose another store to visit, but if is the same already visited loop random.choice until its not the case
        while now_this in client.no_go:
            now_this = random.choice(self.stores)
            # But if all available places sucks, go home
            if len(client.no_go) == len(self.stores):
                pass
        # Go shop in this other store
        self.shopping(now_this, client)

    def shopping(self, selected_store, client):
        """
        Emulates the agents wandering trough stores until satisfied with the experience
        given by one of the possible choices
        :param selected_store:  store to visit
        :param client: a given client
        :return:
        """
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
                if selected_store.capacity > 1:
                    selected_store.update_experience()
                    # Update the experience based on store capacity
                else:
                    pass
                    # Avoid error of divide by zero in update_experience formula
                client.exp += selected_store.product()
                # To buy a good it's to get an experience. This experience value its placed within costumer
                # attribute Agent.exp
                stay = client.exp > 5
                # Once it bought something the costumer decides to stay according to the gathered experience
                if not stay:
                    # If the costumer choose to leave, it clears space to a new costumer
                    selected_store.capacity += 1
                    # Go choose other place to go, except that one already visited
                    self.to_other_place(selected_store, client)
                else:
                    pass

    def run_model(self):
        # To every costumer on the list of costumers
        for client in self.customers:
            # Select a random store
            selected_store = random.choice(self.stores)
            # Go shop in this store
            self.shopping(selected_store, client)
        all_means = self.mean_exp(), self.mean_acc(), self.mean_acc(False), self.mean_price()
        to_data(all_means)
        return all_means


if __name__ == '__main__':
    pass
