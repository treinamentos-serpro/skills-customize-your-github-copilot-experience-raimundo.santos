# 📘 Assignment: Testing Python with pytest

## 🎯 Objective

Aprenda a escrever e executar testes automatizados com pytest para verificar funções, cobrir casos de fronteira e investigar falhas. Você também corrigirá um defeito encontrado por um teste.

## 📝 Tasks

### 🛠️ Write your first unit tests

#### Descrição

Prepare um ambiente de prática fora da pasta `assignments/`: copie `starter-code.py`, renomeie a cópia para `starter_code.py` e crie ao lado dela um arquivo chamado `test_starter_code.py`. Instale pytest com `python -m pip install pytest` e escreva testes para `is_even` e `average`.

#### Requisitos
O programa concluído deve:

- Incluir pelo menos dois testes para `is_even`, verificando um número par e um ímpar.
- Verificar o resultado de `average` para uma lista com mais de um número.
- Executar os testes com `python -m pytest -q` e obter sucesso nesta etapa.

### 🛠️ Test boundaries and invalid input

#### Descrição

Amplie a suíte com testes parametrizados e casos de fronteira. Verifique o comportamento de `average` com uma lista vazia e de `discounted_price` com valores válidos e inválidos.

#### Requisitos
O programa concluído deve:

- Usar `pytest.mark.parametrize` para testar múltiplas entradas de pelo menos uma função.
- Confirmar que `average` gera `ValueError` para uma lista vazia.
- Confirmar que `discounted_price` aceita descontos de 0% e 100%.
- Confirmar que preços negativos e descontos fora do intervalo de 0% a 100% geram `ValueError`.

### 🛠️ Diagnose and fix a failing test

#### Descrição

O código inicial contém um defeito intencional: `discounted_price` rejeita um desconto de 100%. Execute os testes, leia a falha, corrija a função e mantenha um teste de regressão para esse caso.

#### Requisitos
O programa concluído deve:

- Demonstrar a falha do teste de desconto de 100% antes da correção.
- Corrigir a função sem remover ou enfraquecer os testes.
- Executar novamente `python -m pytest -q` e obter sucesso em toda a suíte.
