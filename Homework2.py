"""A game that compare a number guessed by the user with the random number between 0 to 100, picked by CPU. Hints are
provided After three fails. """
import random


def hint(t, ans):
    """
    Function that is triggered after three fails. Compares if the guess is above or bellow te right answer
    :param t: the guess by the user
    :param ans: the correct answer
    :return: a print statement with a hint to the user.
    """
    if t > ans:
        print(f"\n<<<<<<<<<<<<<< HINT >>>>>>>>>>>>>> \nA resposta certa é menor do que {t}")
    else:
        print(f"\n<<<<<<<<<<<<<< HINT >>>>>>>>>>>>>> \nA resposta certa é maior do que {t}")


def test_guess(ans, count):
    """
    Function that compare the number provided by the user with the one randomly assinged by the program
    :param ans: the correct answer
    :param count: the current counter of times that player is trying
    :return: True when the user fails the guessing and False when the player correctly guess the answer
    """
    t = int(input("\nDigite um número de 0 à 100\n:"))
    if t == ans:
        print(
            f" \n#### A C E R T O U ! #### \n\n@@@@ P A R A B É N S @@@ \n\nDepois de {count} tentativas ficou fácil, "
            f"né!?")
        return False
    if t != ans:
        if count > 3:
            hint(t, ans)
            count += 1
            print('\nPreste atenção na dica e tente de novo!')
        else:
            print("\nNope! Tente mais uma vez!")
            count += 1
        return True


def guessing_game():
    """The interfaface of the program. Here the user will choose to play or to close the game. Invalid options are
    tested. """

    print("Olá! Bem vindo ao jogo da adivinhação!\n\nEu escolho um número e você tenta adivinhar")
    r = input("Vamos começar? \n\nPressione: (1) SIM, ou (0)NÃO\n:")
    if r == '1':
        ans = random.randint(0, 100)
        count = 0
        infinite = True
        while infinite:
            count += 1
            infinite = test_guess(ans, count)
    elif r == '0':
        return False
    elif r != '0' or r != '1':
        print('\n\nHmm, acho que você entrou uma opção inválida! Vamos começar de novo?\n')
        guessing_game()


if __name__ == '__main__':
    guessing_game()
