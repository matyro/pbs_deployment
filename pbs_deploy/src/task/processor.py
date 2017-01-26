##Base Processor with abstract function

from abc import ABC, abstractmethod




class processor(ABC):
        
    @abstractmethod
    def run(self, environment):
        return environment
        
        
    
        
    