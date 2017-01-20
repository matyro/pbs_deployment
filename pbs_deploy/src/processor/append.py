import processor


import shutil

class append (processor):
     
     def __init__(self):
         pass
         
     def run(self):
         with open(self.settings['from'], 'r') as readFile:
             data = readFile.read()
             
             with open(self.settings['to'], 'w') as writeFile:
                 writeFile.append(data)
         
         
     
     def set(self, name, para):
         self.settings[name] = para