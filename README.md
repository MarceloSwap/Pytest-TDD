# Pytest-TDD

Projeto em **Python** para praticar **TDD (Test Driven Development)** com `pytest`.

## Objetivo
Criar uma classe *Calculadora* aplicando o ciclo do **TDD**:

1. **Escrever os testes** primeiro (*test_calculadora.py*).
2. **Executar os testes** (eles falham porque ainda não há implementação).
3. **Implementar o código mínimo** na classe *Calculadora* para passar nos testes.
4. **Reexecutar os testes** até que todos passem.
5. **Refatorar se necessário**.


## Como rodar

### Clone este repositório:
    git clone https://github.com/MarceloSwap/Pytest-TDD.git
    cd Pytest-TDD
    pip install pytest
    ###  rodar os testes
    pytest -v

### saída esperada
    test_calculadora.py::TestCalculadora::test_soma PASSED
    test_calculadora.py::TestCalculadora::test_subtracao PASSED
    test_calculadora.py::TestCalculadora::test_multiplicacao PASSED
    test_calculadora.py::TestCalculadora::test_divisao PASSED
    test_calculadora.py::TestCalculadora::test_divisao_por_zero PASSED

![Execução dos testes](assets/image.png)
