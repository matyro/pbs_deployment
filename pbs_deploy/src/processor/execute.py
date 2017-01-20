import processor


import subprocess
import os

import subprocess, os


class execute (processor):
     
     def __init__(self, name):
         self.name = name
         pass
         
     def run(self):
         parameter = ''
         for key, value in self.settings.items():
             parameter = parameter + '-' + str(key) + str(value)
             
         my_env = os.environ.copy()
         ##my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
         subprocess.Popen(self.name + ' ' + oarameter, env=my_env)
         
     
     def set(self, name, para):
         self.settings[name] = para