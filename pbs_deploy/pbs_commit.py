
import xml.etree.ElementTree as ET

from src import process




def main():

	xmlPath = sys.argv[1]
	id_list = sys.argv[2]

	tree = ET.parse(xmlPath)
	root = tree.getroot()

	process_list = []
	environment = parse_env(root)   

	for itr in root.findall('./process'):   
		tmp = Process(environment, itr)
    
		tmp.set_arguments(itr.attrib)  
        
		process_list.append( tmp )


	for proc in process_list:

	with open(id_list, 'r') as file:
		for file_id in file:
            		print('ID: ' + file_id)            
			tmp = {'id': file_id.strip()}
			proc.update_env(tmp)
                       
			proc.run()
			break






if __name__ == "__main__":
	main()
