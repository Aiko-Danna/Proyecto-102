import os;
import shutil;

from_dir = "/Users/danna/Downloads"
to_dir = "/Users/danna/Documents/Documents/Danna/Archivos_Documentos"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    #print(name)
    #print(extension)
    
    if extension == "":
        continue
    
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        ruta1 = from_dir + "/" + file_name
        ruta2 = to_dir + "/" + "Archivos_Documentos"
        ruta3 = to_dir + "/" + "Archivos_Documentos" + "/" + file_name
        
        #print("ruta1", ruta1)
        
        #Verificar si la carpeta/directorio existe antes de mover
        #Si no, crea una nueva carpeta/directorio y luego mueve
        if os.path.exists(ruta2):
            print("Moviendo " + file_name + ".....")
        
            #Move from ruta1 ---> ruta3
            shutil.move(ruta1, ruta3)
        
        else:
            os.makedirs(ruta2)
            print("Moviendo " + file_name + ".....")
            shutil.move(ruta1, ruta3)