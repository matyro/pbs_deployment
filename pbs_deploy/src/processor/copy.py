import processor


import shutil

class copy (processor):
     
     def __init__(self):
         pass
         
     def run(self):
         shutil.copy(self.settings['from'], self.settings['to'])
         
     
     def set(self, name, para):
         self.settings[name] = para