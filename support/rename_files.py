import os
path = 'D:\do this\pemutih' 
os.chdir(path)
print(os.getcwd())
 
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    
    f_name = "pemutih" + str(count)
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
