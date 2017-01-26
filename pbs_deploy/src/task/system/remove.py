import processor


import shutil

class remove (processor):
     
     def __init__(self):
         pass
         
     def run(self):
         shutil.rmtree(self.settings['path'])
         
     
     def set(self, name, para):
         self.settings[name] = para