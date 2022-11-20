#Automation

from distutils import extension
import os
import shutil
'''
folder_path='projekt2'
os.chdir(folder_path)

os.mkdir('Images')
os.mkdir('Dokuments')
os.mkdir('videos')
os.mkdir('comperessed')
os.mkdir('files')
os.mkdir('Coding')

for file in os.listdir('.'):
   
    
   
    if file.endswith(('.png','.jpg','.gif','.jpeg')):
        shutil.move(file,'Images')

    elif file.endswith(('.pdf','.epib','.word','.docs','.xlsx','.pptx')):
        shutil.move(file,'Dokuments')

    elif file.endswith(('.mp4','.avi')):
        shutil.move(file,'videos')

    elif file.endswith(('.rar','.zip')):
        shutil.move(file,'comperessed')

    elif file_extention in['.csv','.otf']:
        shutil.move(file,'files')

    elif file.endswith(('.py','.html','.css')):
        shutil.move(file,'Coding')

print('done')  
'''
##new style
def working_dir(path):
    os.chdir(path)
    print(f'Moved to:{path}')

def check_folder():
    folder=['Images','Dokuments','videos','comperessed','files','Coding']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

def get_extentions():
    extensions=[]
    for file in os.listdir('.'):
        filename,file_extention=os.path.splitext(file)
        if file_extention not in extension:
            extension.append(file_extention)
    print(extension)
    

def organize():
    
  for file in os.listdir('.'):
   
    
   
    if file.endswith(('.png','.jpg','.gif','.jpeg')):
        shutil.move(file,'Images')

    elif file.endswith(('.pdf','.epib','.word','.docs','.xlsx','.pptx')):
        shutil.move(file,'Dokuments')

    elif file.endswith(('.mp4','.avi')):
        shutil.move(file,'videos')

    elif file.endswith(('.rar','.zip')):
        shutil.move(file,'comperessed')

    elif file_extention in['.csv','.otf']:
        shutil.move(file,'files')

    elif file.endswith(('.py','.html','.css')):
        shutil.move(file,'Coding')
  print('done')  

def main():
    working_path = input('Enter path:  ')
   
    working_dir(working_path)
    check_folder()
    get_extentions()
    organize()

if __name__== '__main__':
    main()
