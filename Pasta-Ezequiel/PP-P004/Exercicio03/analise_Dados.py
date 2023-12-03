
from abc import ABC, abstractmethod

class AnaliseDados(ABC):
    def __init__(self, tipoDeDados):
        self._tipoDeDados = tipoDeDados
        self._dados = []

    @property
    @abstractmethod
    def label(self):
        pass

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def calcularMediana(self):
        pass
    @abstractmethod
    def listarEmOrdem(self):
        pass
    
    def __iter__(self):
        return iter(self._dados)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._tipoDeDados}) - Dados: {self._dados}"

    def __len__(self):
        return len(self._dados)
