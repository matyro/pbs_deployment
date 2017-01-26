

import xml.etree.cElementTree as ET





class Run():
    
    def __init__(self, xml_file, env = dict()):          
        self.environment = env.copy()
        
        
        
        
             
    def write_config(self, path):
        xml_string = ET.tostring(self.run_config).decode("utf-8") 
        xml_string.format(**self.local_env)
        
        #new_xml = ET.fromstring(xml_string)        
           
        name = path + '/' + self.name + '_' + self.local_env['id'] + '.card'
        
        with open(name.format(**self.local_env), 'w') as file:
            file.write(xml_string)
            
        
        return name
    
    
    

	if 'exec' in xm.attrib:
		self.executable = xml.attrib['exec']
	else
		raise XML_Exception('No exec field on run element!')

	





    def parse_xml(self, xml_data):
        
        
        
        
        
        
