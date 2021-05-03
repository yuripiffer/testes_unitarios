def soma(n1,n2):
    return n1 + n2


def raiz(n1):
    if not isinstance(n1, (int,float)):
        raise TypeError
    elif n1 < 0:
        raise ValueError

    return n1 ** 0.5


# FUNÇÃO SEM RETORNAR NADA
# Isso é meio errado ... o bom era retornar true or false
lista = []
def listadef(n):
    lista.append(n)

lista2 = [""]
def listadef2(n):
    try:
        lista2[n]
        return True
    except:
        return False

from random import randint
def muitas_strings(string):
    return string * randint(1, 100)