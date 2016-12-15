from . import exception


def parse_env(xml):
    xml_env = xml.findall('environment')
    env = dict()
    
    if len(xml_env) > 1:
        raise XML_Error('Found more then one global environment')
    elif len(xml_env) == 1:
        for itr in xml_env[0]:
            try:        
                print(str(itr.tag) + ': ' + str(itr.get('name')) + ' width ' + str(itr.text) )
                env[ str(itr.get('name')) ] = str(itr.text)
            except:
                raise  
    return env
