#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PIL
from PIL import Image
from os import listdir
from threading import Thread
import threading
import time


def main():
    i=0
    path = r'image net data\unsplash-research-dataset-lite-latest\downloaded'
    fin_path = r'prepared background\\'

    files = [f for f in listdir(path)]

    while i<16000:
        for file in files:
            name = path+'\\'+file
            while threading.active_count() >=30:
                time.sleep(10)
            with Image.open(name) as image:
                width, height = image.size
                if height > 2*720 and width > 2*1280:
                    Thread(target=process_image, args=(i,name,fin_path)).start()
                    i+=4
            if i>=16000:
                break
        
def process_image(i,name,fin_path):
    with Image.open(name) as image:
        #1st image
        new_image = image.crop((0, 0, 1280, 720))
        new_image.save(fin_path+str(i)+'.jpg','JPEG')
        #2nd image
        new_image = image.crop((1280, 0, 2560, 720))
        new_image.save(fin_path+str(i+1)+'.jpg','JPEG')
        #3rd image
        new_image = image.crop((0, 720, 1280, 1440))
        new_image.save(fin_path+str(i+2)+'.jpg','JPEG')
        #4th image
        new_image = image.crop((1280, 720, 2560, 1440))
        new_image.save(fin_path+str(i+3)+'.jpg','JPEG')
    print(i+4)
    
if __name__ == '__main__':
    main()

