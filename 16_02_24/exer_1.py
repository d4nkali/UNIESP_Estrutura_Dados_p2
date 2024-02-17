# Exercicio 1  - Objetos em Python

class Aluno:  # Cria a classe Aluno
  # Com o construtor, define 3 parametros(nome, nota1 e nota2)
  def __init__(self, nome, nota1, nota2): 
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2
    self.media = 0.0


  def calcular_media(self): # Cria a função de calcular a media das notas
    self.media = (self.nota1 + self.nota2) / 2   # Define que 'media' sera ('nota1' + 'nota2') / 2
    return self.media # Guarda o resultado em 'media'


  def mostrar_dados(self): # Cria a função de mostrar dados
    print(f"Nome: {self.nome}") # Imprime o nome
    print(f"Nota1: {self.nota1}") # Imprime a primeira nota
    print(f"Nota2: {self.nota2}") # Imprime a segunda nota
    print(f"Média da Nota: {self.media}") # Imprime a media


  def resultado(self): # Cria a função de resuntados
    if self.media >=7: # Se a media for maior ou igual a 7, então:
      print("Aluno(a) aprovado(a)") # Imprime que esta aprovado
    else: # Senão
      print("Aluno(a) reprovado(a)")  # Imprime que não esta aprovado


# Criando os objetos
      
aluno1 = Aluno("Carlos", 9.0, 8.7)  # Cria o objeto aluno1 com os parametros ("Carlos", 9.0, 8.7)
aluno2 = Aluno("Paula", 9.5, 5.5)   # Cria o objeto aluno2 com os parametros ("Paula", 9.5, 5.5) 
aluno3 = Aluno("Helena", 10.0, 8.0) # Cria o objeto aluno3 com os parametros ("Helena", 10.0, 8.0)


# Executar as funções e Imprimir os Resultados
aluno1.calcular_media()
aluno1.mostrar_dados()
aluno1.resultado()

aluno2.calcular_media()
aluno2.mostrar_dados()
aluno2.resultado()

aluno3.calcular_media()
aluno3.mostrar_dados()
aluno3.resultado()

# FIM!