import processor


import shutil

class move (processor):
     
     def __init__(self):
         pass
         
     def run(self):
         shutil.move(self.settings['from'], self.settings['to'])
         
     
     def set(self, name, para):
         self.settings[name] = para