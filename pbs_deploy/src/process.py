

import os

from . import functions
from . import run




class Process():
    def set_arguments(self, arg):
        self.arguments = '-m a'
        
        for key, value in arg.items():                        
            print(key + ': ' + value)
                        
            if key == 'name':
                self.arguments = self.arguments + ' -N ' + value
            elif key == 'stdout':                
                self.arguments = self.arguments + ' -o ' + value
            elif key == 'stderr':
                self.arguments = self.arguments + ' -e ' + value
            elif key == 'arguments':
                self.arguments = self.arguments + ' ' + value
    
    def update_env(self,env):
        self.local_env.update( env )
        for itr in self.run_list:
            itr.update_env(env)
        
    
    def run(self):
        self.arguments.format(**self.local_env)
        config = '"'
        for itr in self.run_list:
            config = config + ',' + itr.write_config(self.config_path)
        config = config + '"'
        os.system('qsub ' + self.arguments + ' -v config=' + config + ' ~/deploy/run.py')
        
    
    
    def __init__(self, env, xml):        
        self.local_env = env.copy()
        self.local_env.update( parse_env(xml) )
        
        self.run_list = [Run(self.local_env, run_xml) for run_xml in xml.findall('run') ]
        
        self.config_path = xml.attrib['config']
              
    
