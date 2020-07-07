import random
from Exercise2.Loja import Loja
from Exercise2.Agent import Agent


class Simulacao:
    def __init__(self):
        self.lojas = list()
        self.clientes = list()
        self.criar_lojas()
        self.criar_agentes()
        self.deposito_inicial()

    def salvar_arquivo_dados(self):
        # TODO: Create a .txt with the run results
        # with open('arquivo1.csv', 'w') as handler as f:
        pass

    def criar_lojas(self):
        for id in range(10):
            self.lojas.append(Loja(id))

    def criar_agentes(self):
        for id in range(10):
            self.clientes.append(Agent(id))

    def media_experiencia(self):
        experiencia_somada = 0
        for client in self.clientes:
            experiencia_somada += client.exp
        return experiencia_somada / len(self.clientes)

    def deposito_inicial(self):
        for client in self.clientes:
            client.acc.deposit(random.randint(10, 20))

    def run_model(self):
        # TODO: Agent choose to stay in the store or buy something else in another place
        for client in self.clientes:
            loja_escolhida = random.choice(self.lojas)
            posso_ir = loja_escolhida.capacity_check()
            if posso_ir:
                if client.check_funds(loja_escolhida):
                    loja_escolhida.acc.deposit(client.acc.draw_cash(loja_escolhida.cost_product))
                    client.exp += loja_escolhida.product()
        return self.media_experiencia()


if __name__ == '__main__':
    minha_sim = Simulacao()
    media = minha_sim.run_model()
    print(media)
