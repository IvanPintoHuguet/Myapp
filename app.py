import customtkinter as ctk
import tkinter as tk
from PIL import ImageTk
from functions import *

def plot_image():
    global picture
    
    img = search_picture()
    picture = ImageTk.PhotoImage(img, master = root)
    label_image.configure(image = picture)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry('300x300')
root.title('App')

'''================ Frame to search files ========================='''
    
frame_files = ctk.CTkFrame(master=root)
frame_files.pack()

#Button to search file
ctk.CTkButton(frame_files, text = 'Search picture', cursor="hand2",  command = plot_image).pack(pady=5, padx=5)

#Image
label_image = tk.Label(root, bg = '#222325')
label_image.pack()

'''==============================================================='''



root.mainloop()