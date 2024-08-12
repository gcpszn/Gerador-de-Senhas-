from random import choice # Importa a biblioteca para gerar números aleatórios

print('-' * 20)
print('GERADOR DE SENHAS'.center(20,' ')) # Cabeçalho do programa
print('-' * 20)

while True:
	tam = int(input('Quantos caracteres serão necessários? [mínimo 4 a máximo 12 caracteres]: '))  # Solicita ao usuário o comprimento desejado para a senha
	if 4 <= tam <= 12:	# Verifica se o comprimento está dentro do intervalo permitido
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
	
	
	
		
