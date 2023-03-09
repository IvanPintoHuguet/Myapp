import os
from tkinter import ttk, filedialog
from PIL import Image

  

def search_picture():
    filepath = filedialog.askopenfilenames(title='Select file', filetypes=[("jpg files", ".jpg")])
    try: 
        img = Image.open(filepath[0])
        size = img.size
        r = size[0]//150
        return img.resize((size[0]//r, size[1]//r))
    except: pass
    