

import xml.etree.ELementTree as ET

from . import functions
from . import exception



class Run():
    
    def update_env(self,env):
        self.local_env.update( env )
        
        
    def write_config(self, path):
        xml_string = ET.tostring(self.run_config).decode("utf-8") 
        xml_string.format(**self.local_env)
        
        #new_xml = ET.fromstring(xml_string)        
           
        name = path + '/' + self.name + '_' + self.local_env['id'] + '.card'
        
        with open(name.format(**self.local_env), 'w') as file:
            file.write(xml_string)
            
        
        return name
    
    
    def __init__(self, env, xml):          
        self.run_config = xml
        self.local_env = env.copy()
        self.local_env.update( parse_env(xml) )
        self.name = xml.attrib.get('name', '')

	if 'exec' in xm.attrib:
		self.executable = xml.attrib['exec']
	else
		raise XML_Exception('No exec field on run element!')

	







