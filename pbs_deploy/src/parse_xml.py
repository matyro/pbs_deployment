import xml.etree.ElementTree as ET






def str_to_class(name):
    class_name_list = [cls.__name__ for cls in vars()['Processor'].__subclasses__()]
    
    try:
        position = class_name_list.index(name)
    except ValueError:
        raise IndexError
    
    class_list = vars()['Processor'].__subclasses__()
    return class_list[position]



from functools import singledispatch
@singledispatch
def parse_xml_block(xml_data):
    root = ET.fromstring(xml_data)
    parse_xml_block(root)
    
    
        
@parse_xml_block.register(ET.Element)
def _(root):      
    execution_list = []
    
    proc = str_to_class(root.tag)()
    for setting, parameter in root.attrib.items():
        try:
            getattr(proc, setting)
            setattr(proc, setting, parameter)
        except:
            print('Setting ' + setting + ' was not found for class ' + str(proc) )
            pass
        
    execution_list.append(proc)
    
    for child in root:
        execution_list.append( parse_xml_block(child) )
    
    return execution_list
    