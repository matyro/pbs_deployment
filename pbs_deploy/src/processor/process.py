## Job class starts a pbs task

from . import processor

class process (processor):
     
     def __init__(self):
         pass
         
     def run(self):
        pbs.start(
         
     
     def set(self, name, para):
         self.settings[name] = para