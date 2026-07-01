import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {} # Aqui guardamos a nossa lista/coleção de objetos
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        # Salva o dicionário no arquivo
        with open(self.__datasource, 'wb') as file:
            pickle.dump(self.__cache, file)

    def __load(self):
        # Carrega o dicionário do arquivo
        with open(self.__datasource, 'rb') as file:
            self.__cache = pickle.load(file)

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            return None

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.__cache.values()