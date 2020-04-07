import os,shutil

#Enter The Path here
path =r'C://path'

_list=os.listdir(path)

for file in _list:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=='':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+ '/' +ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
