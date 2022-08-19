"""
Classes de animais
"""

import pandas as pd
import numpy  as np

class Cachorro:

    def __init__ (self, nome = 'Jorge'):
        self.nome = nome
    
    def latir(self):
        print("Au au")

    def nome(self):
        print(f'{self.nome}')
