from os import listdir
from os.path import isfile, join
import os


## select only files we want to encrypt
onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
index_dot = 0
onlyimg = []
list_format_img = ["jpg","png","jpeg","gif","jfif","mp4","avi"] #list of format
print(onlyfiles)
for name in onlyfiles:
    for l in range(len(name)):
        if name[l] == '.':
            index_dot = l
    format_img = len(name)-index_dot-1

    if name[-format_img:] in list_format_img:
        onlyimg.append(name)
print(onlyimg)


# encrypt those files
key1 = int(input('password:'))
for to_work_on in onlyimg:     
    try:
        path = to_work_on
        key0 = 5
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ key1 + key0  ## change this line to create your own encrypt method
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
     
         
    except Exception:
        print('Error : ', Exception.__name__)
        
