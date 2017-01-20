
from abc import ABCMeta, abstractmethod




class processor:
        
    @abstractmethod
    def run(self, data_dict):
        return data_dict
        
        
    @abstractmethod
    def set(self, name, para):
        self.settings[name] = para
    