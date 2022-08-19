"""
Classes de animais
"""

import pandas as pd
import numpy  as np

class Cachorro(self):
    
    def __init__ (self, name):
        self.name = name
    
    def latir(self):
        print('Au!Au!')
        
    def nome(self):
        print(f'{self.name}')