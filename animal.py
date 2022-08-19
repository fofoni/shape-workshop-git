"""
Classes de animais
"""

class Topeira:
    def __init__(self):
        self.nome = "ruffus"
        self.funcao = "salvar o Ron"
        self.desenho = "Kim Possible"
        
class Cachorro:

    def __init__ (self, nome = 'Jorge'):
        self.nome = nome
    
    def latir(self):
        print("Au au")

    def nome(self):
        print(f'{self.nome}')
        