# Gerador de Senhas

## Descrição

Este script em Python é um gerador de senhas aleatórias que permite ao usuário especificar o comprimento desejado da senha. O comprimento da senha deve estar entre 4 e 12 caracteres. O script utiliza a função `choice` da biblioteca `random` para gerar senhas aleatórias a partir de um conjunto predefinido de caracteres que inclui letras minúsculas, números e caracteres especiais.

## Funcionalidades

- Solicita ao usuário o comprimento desejado da senha.
- Gera uma senha aleatória com base no comprimento informado.
- Exibe a senha gerada.
- Permite ao usuário tentar gerar uma nova senha ou encerrar o programa.

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone o repositório ou faça o download do arquivo `geradordesenhas.py`.
3. Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo está localizado.
4. Execute o script com o comando:

    ```bash
    python geradordesenhas.py
    ```

5. Siga as instruções exibidas na tela para gerar a senha.

## Código

Aqui está o código do gerador de senhas:

```python
from random import choice # Importa a biblioteca para gerar números aleatórios

print('-' * 20)
print('GERADOR DE SENHAS'.center(20, ' ')) # Cabeçalho do programa
print('-' * 20)

while True:
    tam = int(input('Quantos caracteres serão necessários? [mínimo 4 a máximo 12 caracteres]: '))  # Solicita ao usuário o comprimento desejado para a senha
    if 4 <= tam <= 12:  # Verifica se o comprimento está dentro do intervalo permitido
        senha = '' # Inicializa a variável para armazenar a senha gerada
        caracteres = 'qwertyuiopasdfghjklçzxcvbnm.789456123!@#$%*' # Conjunto de caracteres permitidos para a senha
        
        for digito in range(tam): # Executa o loop 'tam' vezes para gerar a senha com o número de caracteres desejado pelo usuário
            aleatorio = choice(caracteres) # Seleciona um caractere aleatório 
            senha += aleatorio # Adiciona o caractere à senha

        print('-' * 30)
        print(f'Senha gerada: {senha}') # Exibe a senha gerada
        print('-' * 30)
        break  # Sai do loop se a senha foi gerada com sucesso
    else:
        print('Número de caracteres inválido. Mínimo 4 e Máximo 12.')  # Informa ao usuário que o valor é inválido e solicita um novo 
        
    continuar = str(input('Deseja tentar novamente? [S/N]: ')).strip().upper() # Pergunta ao usuário se deseja tentar novamente
    if continuar != 'S':
        print('Encerrando o programa...')
        break # Encerra o programa se o usuário não quiser continuar
