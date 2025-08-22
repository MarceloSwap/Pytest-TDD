import pytest
from calculadora import Calculadora

class TestCalculadora:

    def setup_method(self):
        self.calc = Calculadora()

    def test_soma(self):
        assert self.calc.somar(2, 3) == 5

    def test_subtracao(self):
        assert self.calc.subtrair(10, 5) == 5

    def test_multiplicacao(self):
        assert self.calc.multiplicar(4, 3) == 12

    def test_divisao(self):
        assert self.calc.dividir(10, 2) == 5

    def test_divisao_por_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.dividir(10, 0)
