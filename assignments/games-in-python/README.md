
# 📘 Assignment: Python Hangman

## 🎯 Objective

Pratique strings, listas, seleção aleatória, condicionais e loops ao criar um jogo da forca em Python. O jogador tentará descobrir uma palavra secreta antes de esgotar as tentativas disponíveis.

## 📝 Tasks

### 🛠️ Prepare a palavra e o estado do jogo

#### Descrição
Use a lista de palavras do arquivo `starter-code.py` para selecionar uma palavra secreta aleatoriamente. Inicialize as variáveis necessárias para registrar as letras descobertas, os erros e o limite de tentativas.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista predefinida.
- Acompanhar as letras já informadas e o número de palpites incorretos.
- Exibir o progresso da palavra, mostrando letras descobertas e espaços para as demais, por exemplo: `_ _ _`.

### 🛠️ Implemente o loop de palpites

#### Descrição
Implemente o loop principal para receber palpites, atualizar o progresso e encerrar o jogo quando o jogador vencer ou ficar sem tentativas.

#### Requisitos
O programa concluído deve:

- Solicitar ao jogador um palpite de letra e verificar se ela pertence à palavra secreta.
- Atualizar o progresso quando o palpite estiver correto e contabilizar um erro quando estiver incorreto.
- Encerrar quando todas as letras forem descobertas ou quando o limite de erros for atingido.
- Exibir uma mensagem indicando vitória ou derrota e revelar a palavra secreta ao final.