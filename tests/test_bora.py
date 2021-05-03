from unittest import TestCase, mock
from funcoes.bora import *

class TestandoBora(TestCase):

    def test_soma_is_working(self):
        n1 = 10
        n2 = 12
        self.assertEqual(soma(n1,n2),22)

    def test_raiz_funciona(self):
        type_test = "a"
        with self.assertRaises(TypeError):
            raiz(type_test)

        value_test = -9
        with self.assertRaises(ValueError):
            raiz(value_test)

        self.assertEqual(raiz(144),12)

    #isso de puxar variável global dá problema
    def test_lista(self):
        listadef(1)
        self.assertEqual(lista, [1])

    def test_lista2(self):
        self.assertTrue(listadef2(0))
        self.assertFalse(listadef2(1))

    #FAZ COM QUE ALGO ALEATÓRIO VENHA NUM VALOR FIXO PARA FAZER O TESTE
    # @mock.patch(nome_arquivo.nome_funcao.nome_coisa_importada, return_value = valor a ser mocado)
    @mock.patch("funcoes.bora.randint", return_value = 2)
    def test_muitas_strings_works(self, mock_rand):
        self.assertEqual(muitas_strings("ABC"), "ABCABC")

        # #CHECAR SE O MOCK FOI CHAMADO
        # mock_rand.assert_any_call() # se ele foi chamado
        # mock_rand.assert_called_once ...
        # mock_rand.assert_called_once_with(1,100) #se foi chamado de 1 a 100
        # mock_rand.assert_has_calls(2)  # se foi chamado de 2
        # mock_rand.assert_has_calls(mock.call(1,2), mock.call(1,100))


