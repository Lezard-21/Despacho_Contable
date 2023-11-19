from tkinter import *
from PIL import Image, ImageTk


def create_rectangle(root,canvas,x1, y1, x2, y2, **kwargs):
    images = [] # Para mantener la imagen creada
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        r, g, b = root.winfo_rgb(fill)
        fill = (r//256, g//256, b//256, alpha)
        width = round(x2-x1)
        height = round(y2-y1)
        image = Image.new('RGBA', (width, height), fill)
        images.append(ImageTk.PhotoImage(image))
        canvas.create_image(x1, y1, image=images[-1], anchor='nw')
    canvas.create_rectangle(x1, y1, x2, y2, **kwargs)