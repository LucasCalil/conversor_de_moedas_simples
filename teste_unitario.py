import unittest
from conversor import ConversorDeMoedas 

class TestConversorDeMoedas(unittest.TestCase):

    def test_conversao_usd_para_brl(self):
        conversor = ConversorDeMoedas('USD', 'BRL', 100)
        resultado = conversor.converter()
        self.assertEqual(resultado, 525.00)

    def test_conversao_brl_para_eur(self):
        conversor = ConversorDeMoedas('BRL', 'EUR', 100)
        resultado = conversor.converter()
        self.assertEqual(resultado, 16.00)

    def test_mesma_moeda_sem_conversao(self):
        conversor = ConversorDeMoedas('USD', 'USD', 100)
        resultado = conversor.converter()
        self.assertEqual(resultado, 100)

    def test_conversao_invalida(self):
        conversor = ConversorDeMoedas('USD', 'JPY', 100)
        with self.assertRaises(ValueError):
            conversor.converter()

    def run_tests(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestConversorDeMoedas)
        unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    TestConversorDeMoedas().run_tests()
