# Questão 10 - Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador.
# O programa deve solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do 
# computador e determinar o vencedor

# Aluno: Danilo Pereira Viana - P2-B


# Importando biblioteca random
from random import choice

# Imprime uma mensagem de boas vindas
print("Olá :), Bem-vindo ao Jogo Pedra, Papel e Tesoura! (Jokenpo)")

# Cria uma lista com as opções de jogadas
list_acoes = ['Pedra', 'Papel', 'Tesoura']

# Pergunta para o usuario qual ação ele ira realizar e armazena em uma variavel com a formatação correta
acao_user = input("Escolha: Pedra, Papel ou Tesoura? ").capitalize()


if acao_user not in list_acoes: # Se o usuario digitar errado, então:

    print("Escolha inválida. Tente novamente.") # Imprime que esta errado

else: # Se respondeu certo:

    acao_cpu = choice(list_acoes) # O computador escolhe uma das ações atravez do choise

    print(f"\nVocê escolheu: {acao_user}") # Imprime qual foi minha ação
    print(f"O computador escolheu: {acao_cpu}") # Imprime qual foi a ação escolhida pelo computador

    if acao_user == acao_cpu: # Se os dois jogarem igual

        print("Empate!") # Imprime que empatou

    # Se jogar a ação e ganhar:
    elif (acao_user == 'Pedra' and acao_cpu == 'Tesoura') or \
         (acao_user == 'Papel' and acao_cpu == 'Pedra') or \
         (acao_user == 'Tesoura' and acao_cpu == 'Papel'):
        
        print("Você venceu!") # Imprime que o usuario venceu

    else: # Senão:

        print("Você perdeu!") # Imprime que o usuario perdeu

# FIM!