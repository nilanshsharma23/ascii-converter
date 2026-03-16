import tkinter as tk
from tkinter import filedialog
import convert
import cv2

root = tk.Tk()

root.title("Image to ASCII")

b = tk.Label(root, text="path: ")

a = ""
txt = tk.Text(root, font=("monospace", 2), width=900, height=900)

def select_image():
    global a
    a = filedialog.askopenfilename()
    b.config(text=f"path: {a}")
    
    img = cv2.imread(a)
    small = cv2.resize(img, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_AREA)
    # height, width, _ = small.shape
    txt.insert('1.0',convert.convert(small))

select = tk.Button(root, text="Select Image", command=select_image)
select.pack()

b.pack()

txt.pack()

root.mainloop()