#pathlib module

#mkdir - to create directory
#rmdir - to delete directory
from pathlib import Path
#Absolute path
#c:\Program Files\Microsoft
#relative path

#path = Path("ecommerce")
#path = Path("emails")
#print(path.exists()) #its exists or not
#print(path.mkdir())
#print(path.rmdir())

path = Path()
for file in path.glob('*.py'): # here * will take all the files.not the directories
    print(file)



