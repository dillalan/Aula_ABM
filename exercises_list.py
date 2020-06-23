"""
1. Escreva um programa que imprima o seguinte padrão.
 *
 * *
 * * *
 * * * *
 * * *
 * *
 *

2. Altere o programa acima para que o usuário possa entrar com o número máximo de estrelas.

3. Escreva um programa que corre os números de 23 a 83 e imprime. Mas, quando for múltiplo
de três, imprima ‘Pum’, quando for múltiplo de 5 imprima ‘Bla’, quando for de ambos
imprima ‘PumBla’.

4. Escreva um programa que ache e imprima os números divisíveis por 13 e por 19, entre o ano
de nascimento da sua mãe e 2727.

5. Escreva um programa que recebe uma letra e identifica se ela é consoante.

6. Escreva um programa que conte o número de letras de uma string e retorne e imprima o
valor multiplicado por 10.

7. Escreva um programa que, dada uma lista de números [-2, 34, 5, 10, 5, 4, 32] qualquer,
retorne: o primeiro valor, o número de valores, o último valor, a soma, a média e a mediana.
*** Obs. Para listas com tamanho ímpar, a mediana é o valor do meio, quando ordenada
(sorted()). Para listas pares, retorne os dois valores do meio.

8. Dicionários. Dado o dicionário: d = {‘a’: 0}: faça programas que
8.1 acrescente um par (chave, valor) {‘b’: 1}, ao dicionário;
8.2 verifique se a key ‘c’ está presente?
8.3 Concatene um dicionário a um outro dicionário: e = {z : 23}. Use o método
‘update’!

9. Escreva uma função que faz um loop sobre as keys de um dicionário. Se as keys forem
vogais, eleve o valor ao quadrado. Caso contrário, set o valor para 0. Use if k in ‘aeiou’.

10. Escreva uma função que retorna os máximos e mínimos de um dicionário.

11. Escreva uma função que recebe uma lista e organiza os valores em keys e conta a frequência
de cada uma. Por exemplo: a lista [0, 0, 1, 1, 1, 2, 5], resultaria em: {1: 3, 0: 2, 2: 1, 5: 1}.

12. Escreva uma função que liste todos os números primos até 258 (mais o dia do seu
aniversário). Utilize a divisão modular (%).

13. Escreva um programa que substitua ‘,’ por ‘.’ e ‘.’ por ‘,’ em uma string. Exemplo: 1,000.54
por 1.000,54.

14. Escreva um programa que verifica se todas as letras do alfabeto constam no mínimo uma
vez do parágrafo fornecido pelo usuário.
"""


def star_sky():
    for star in range(1, 4):
        print(star * '* ')
    for star in range(1, 4 + 1):
        print((4 - star + 1) * '* ')


def print_n(n):
    for i in range(1, n + 1):
        print('* ', end='')


def counting_stars(y):
    x = 0
    z = 2
    for line in range(1, 8):
        if 0 < line < 5:
            if (y - x) > line:
                print(line * '* ')
                x += line
            else:
                print_n(y - x)
                break
        if line >= 5:
            if (y - x) >= (line - z):
                print((line - z) * '* ')
                x += (line - z)
                z += 2
            else:
                print_n(y - x)
                break


def star_sky2():
    select = input(
        "Digite:\n[0]Deseja alterar o tamanho do padrão?\n[1]Deseja escolher quantas estrelas são impressas?")
    if select == '1':
        y = int(input("Do total de 16 estrelas, quantas deseja imprimir ao total?"))
        if y > 16:
            print('Não posso repetir o padrão com mais de 16 estrelas')
        else:
            counting_stars(y)
    elif select == '0':
        n = int(input('Quantas estrelas deseja imprimir na linha central do padrão?'))
        n = int(n)
        for star in range(1, n):
            print(star * '* ')
        for star in range(1, n + 1):
            print((n - star + 1) * '* ')
    else:
        star_sky2()


def pumbla():
    for i in range(23, 84):
        if i % 5 == 0 and i % 3 == 0:
            print('PumBla')
        elif i % 3 == 0:
            print('Pum')
        elif i % 5 == 0:
            print('Bla')
        else:
            print(i)


def mom_bday():
    print('Entre 1965 e 2727 os números divisiveis por 13 e 19 são:')
    for ano in range(1965, 2728):
        if ano % 13 == 0 and ano % 19 == 0:
            print(ano)


def is_consonant():
    letra = input('Insira uma letra:\n>')
    vogals = ['a', 'e', 'i', 'o', 'u']
    vogals_cap = ['A', 'E', 'I', 'O', 'U']
    if not letra.isalpha():
        print('Não é letra')
        is_consonant()
    if letra not in vogals and letra not in vogals_cap:
        print(True)
    else:
        print(False)


def str_count(s):
    x = 0
    for character in s:
        if character.isalpha():
            x += 1
            print(character)
    print(x * 10)


def glimpse_list(l):
    sum = 0
    for i in l:
        sum += i
    mean = sum / len(l)
    print(f'A lista contém {len(l)} elementos')
    print(f'O primeiro valor da lista é {l[0]} e o último valor é {l[-1]}')
    print(f'A soma dos elementos da lista é {sum}')
    print(f'A média dos elementos da lista é {mean}')
    if len(l) % 2 == 0:
        l.sort()
        print(f'A mediana da lista é {l[int(len(l) / 2) - 1]} e {l[int(len(l) / 2)]}')
    else:
        l.sort()
        print(f'A mediana da lista é {l[int(len(l) / 2)]}')


def dict_add(d, k, v):
    d['a'] = 0
    d[k] = v


def check_key(k, d):
    if k not in d:
        print(False)
    else:
        print(True)


def concat_dict(d1, d2):
    dcopy = d2.copy()
    for key in d1:
        dcopy.update({key: d1[key]})
    print(d1, '+', d2, '=', dcopy)


def power_vogal(d):
    dpower = d.copy()
    for key in dpower:
        if key in 'aeiou':
            dpower[key] = d[key] ** 2
        else:
            dpower[key] = 0
    print(f'Your input _> {d}')
    print(f'Powervogal _> {dpower}')


def max_min(d):
    b = 0
    c = 0
    for key in d:
        a = d[key]
        if a >= b:
            b = a
        if a <= b:
            if a <= c:
                c = a
    print(f'max _> {b}\nmin _>{c}')


def element_check():
    l = [0, 0, 1, 1, 1, 2, 5]
    d = {}
    l.sort()
    for i in l:
        d[i] = l.count(i)
    print(d)


def primo_to258plus(bday):
    p = [2]
    x = [0]
    for number in range(2, 258 + bday):
        for n in range(2, number):
            y = number % n
            x.append(y)
        if not 0 in x:
            p.append(number)
            x.clear()
        else:
            x.clear()
            pass
    print(p)


def dot_comma(s):
    x = 0
    new_s = ''
    for char in s:
        if s[x] == ',':
            new_s += '.'
        elif s[x] == '.':
            new_s += ','
        else:
            new_s += s[x]
        x += 1
    print(s)
    print(new_s)


def all_alpha(s):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    par_list = []
    for char in s.casefold():
        if char not in par_list:
            par_list.append(char)
    for element in par_list:
        if element in alpha:
            alpha.remove(element)
        else:
            pass
    if len(alpha) > 0:
        print(False)
    else:
        print(True)


if __name__ == '__main__':
    # star_sky()  # 1
    # star_sky2()  # 2
    # pumbla()  # 3
    # mom_bday()  # 4
    # is_consonant()  # 5
    # str_count('Wubba lubba dub dub')  # 6
    # glimpse_list([-2, 34, 5, 10, 5, 4, 32])  # 7
    # d = {'a': 0}  # 8
    # dict_add(d, 'b', 1)  # 8.1
    # check_key('c', d)  # 8.2
    # e = {'z': 23}  # 8.3
    # concat_dict(d, e)  # 8.3
    # f = {'a': -1, 'b': 23, 'e': 6, 'g': -6, 'i': 3}  # 9
    # power_vogal(f)  # 9
    # max_min(f)  # 10
    # element_check()  # 11
    # primo_to258plus(24)  # 12
    # dot_comma('10,050.26')  # 13
    # all_alpha('Quem traz CD, LP, fax, engov e whisky JB?')  # 14
