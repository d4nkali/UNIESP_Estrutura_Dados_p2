'''

Questão 2 -  Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. 
Implemente um método chamado “detalhes” que retorna uma string com as informações do livro.

Aluno: Danilo Pereira Viana - P2-B

'''

class Livro: # Cria a classe Livro

    # Com o construtor, define os seguintes atributos (titulo, autor, resumo)
    def __init__(self, titulo, autor, resumo): 

        self.titulo = titulo
        self.autor = autor
        self.resumo = resumo


    def detalhes(self): # Cria a função 'detalhes'

        # Quando for chamada, imprime os atributos
        return f"Titulo: {self.titulo}\n \nAutor: {self.autor}\n \nResumo: {self.resumo}"


# Cria o objeto 'livro_1' e define os atributos
livro_1 = Livro("O Hobbit", "John Ronald Reuel Tolkien", "Bilbo Bolseiro era um dos mais respeitáveis hobbits de todo o Condado até que, um dia, o mago Gandalf bate à sua porta. A partir de então, toda sua vida pacata e campestre soprando anéis de fumaça com seu belo cachimbo começa a mudar. Ele é convocado a participar de uma aventura por ninguém menos do que Thorin Escudo-de-Carvalho, um príncipe do poderoso povo dos Anãos...")

print("Informações sobre o livro:") # Imprime que vai exebir as informações 
print() # Espaçamento
print(livro_1.detalhes()) # Chama a função 'detalhes'

# FIM!