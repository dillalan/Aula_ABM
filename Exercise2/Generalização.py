from Exercise2 import Simulação


def model_interface(rep=10, agents=100, stores=30):
    """
    A function that runs the main model routine.
    :param rep: (int) 10 by default. The chosen number of times that the model will execute
    :param agents: (int) 100 by default
    :param stores: (int) 30 by default
    :return:
    """
    mean_exp = 0
    mean_acc_client = 0
    mean_acc_store = 0
    mean_price = 0
    sim = Simulação.Simulacao()
    sim.grow_customers(agents)
    sim.grow_stores(stores)
    all_reps_means = tuple()
    for i in range(rep):
        all_reps_means = sim.run_model()
        mean_exp += all_reps_means[0]
        mean_acc_client += all_reps_means[1]
        mean_acc_store += all_reps_means[2]
        mean_price += all_reps_means[3]
        temp = list(all_reps_means)
        temp.clear()
        all_reps_means = tuple(temp)
    print(f'Média Experiencia: {mean_exp/rep}')
    print(f'Média Saldo Conta Cliente: {mean_acc_client/rep}')
    print(f'Média Saldo Conta Loja: {mean_acc_store/rep}')
    print(f'Média de preços: {mean_price/rep}')



if __name__ == '__main__':
    model_interface()

