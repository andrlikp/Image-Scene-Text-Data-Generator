#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import glob
import requests
from IPython.display import clear_output
from threading import Thread

errors = 0

def save_img(row,image_name):
    global errors
    try:
        img_data = requests.get(row).content
        with open('downloaded/'+image_name+'.jpg', 'wb') as handler:
            handler.write(img_data)
    except:
        errors+=1

def main():
    
    global errors
    i=0
    path = './'
    documents = ['photos', 'keywords', 'collections', 'conversions', 'colors']
    datasets = {}

    for doc in documents:
        files = glob.glob(path + doc + ".tsv*")

        subsets = []
        for filename in files:
            df = pd.read_csv(filename, sep='\t', header=0)
            subsets.append(df)

        datasets[doc] = pd.concat(subsets, axis=0, ignore_index=True)
        
    for row in datasets['photos']['photo_image_url']:
        #if i>2000: break
        #if len(row)<3: continue
        #print(row[0].split(',')[0])
        if i<0: #jen podmínka pro ty co už mám stažené, stačí i=0 když není potřeba
            i+=1
            continue
        image_name = datasets['photos']['photo_id'][i]
        Thread(target=save_img, args=(row, image_name)).start()
        clear_output()
        print('saved', " ", i)
        i+=1
        if i>6000+errors:break #zastavovací podmínka
    print('all saved')
    
if __name__ == '__main__':
    main()

