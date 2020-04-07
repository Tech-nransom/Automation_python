import os,shutil

path = r"C://path"  #eg:C:\Users\Downloads
extension = 'mp3'      #eg: zip and not .zip
_list = os.listdir(path)
for files in _list:
    name = files.strip('.' + extension)
    if(os.path.exists(path + '/' + name)):
        continue
    os.makedirs(path + '/' + name)
    shutil.move(path + '/' + files, path + '/' + name + '/' +files)
