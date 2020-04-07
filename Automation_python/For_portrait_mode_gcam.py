import os,shutil

Input_folder = r"H:\\paste"  #Enter The Source Of Folder from which You want to extract the photos form single folders

Output_folder = r"H:\\copy"  #Enter The Destination In which You want Your Extracted Photos

for folder,subfolder,filename in os.walk(Input_folder):      
    for name in filename:
        shutil.copy(os.path.join(folder,name),Output_folder)     



