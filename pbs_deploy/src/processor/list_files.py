import processor


import glob

class list_files (processor):
     
     def __init__(self):
         pass
         
     def run(self, data_dict):
         list = glob.glob(self.settings['path'])
         
     
     
     def set(self, name, para):
         self.settings[name] = para