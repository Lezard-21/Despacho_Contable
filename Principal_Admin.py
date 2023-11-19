
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk

class Principal_Admin:
    def __init__(self, master):
        self.master = master
        self.images = []
        self.canvas = None
        self.crear_interfaz()

    def boton_Ver_Agentes(self):
        #logica del boton
        print("boton_Ver_Agente")

    def  boton_Agregar_Agente(self):
        #logica del boton
        print("boton_agregar_Agente")

    def boton_Ver_Regimen(self):
        #logica del boton
        print("boton_ver_Regimen")

    def boton_Agregar_Regimen(self):
        #logica del boton
        print("boton_Agregar_Regimen")

    def boton_cambiar_informacion(self):
        #logica del boton
        print("boton_Cambiar_informacion")

    def boton_Cerrar_Sesion(self):
        #logica del boton
        print("boton_Cerrar_Sesion")

    def create_rectangle(self, x1, y1, x2, y2, **kwargs):
        if 'alpha' in kwargs:
            alpha = int(kwargs.pop('alpha') * 255)
            fill = kwargs.pop('fill')
            r, g, b = self.master.winfo_rgb(fill)
            fill = (r // 256, g // 256, b // 256, alpha)
            width = round(x2 - x1)
            height = round(y2 - y1)
            image = Image.new('RGBA', (width, height), fill)
            self.images.append(ImageTk.PhotoImage(image))
            self.canvas.create_image(x1, y1, image=self.images[-1], anchor='nw')
        self.canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

    # OUTPUT_PATH = Path(__file__).parent
    # ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame6")

    def crear_interfaz(self):
        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=587,
            width=741,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            391.0,
            293.0,
            image=self.image_image_1
        )

        self.create_rectangle(
            0.0,
            77.0,
            741.0,
            542.0,
            fill="#446575",
            alpha=.8
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Agregar_Agente,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=258.0,
            width=350.0,
            height=100.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Ver_Agentes,
            relief="flat"
        )
        self.button_2.place(
            x=0.0,
            y=393.0,
            width=350.0,
            height=100.0
        )

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_cambiar_informacion,
            relief="flat",
            bg="#446575"
        )
        self.button_3.place(
            x=495.0,
            y=498.0,
            width=243.0,
            height=40.0
        )

        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Cerrar_Sesion,
            relief="flat",
            bg="#446575"
        )
        self.button_4.place(
            x=596.0,
            y=84.0,
            width=145.0,
            height=37.0
        )

        self.button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Agregar_Regimen,
            relief="flat"
        )
        self.button_5.place(
            x=391.0,
            y=260.0,
            width=350.0,
            height=100.0
        )

        self.button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Ver_Regimen,
            relief="flat"
        )
        self.button_6.place(
            x=391.0,
            y=393.0,
            width=350.0,
            height=100.0
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            370.0,
            158.0,
            image=self.image_image_2
        )

    def relative_to_assets(self, path: str) -> Path:
        assets_path = Path(__file__).parent / "assets" / "frame6"
        return assets_path / path
    
if __name__ == "__main__":
    window = Tk()
    window.geometry("740x585")
    window.configure(bg="#FFFFFF")
    window.resizable(False,False)
    # Crea una instancia de IniciarSesion
    app = Principal_Admin(window)

    window.mainloop()
