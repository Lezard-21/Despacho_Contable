from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk


class RegistrarRegimen:

    def __init__(self, master):
        self.master = master
        self.images = []
        self.canvas = None
        self.crear_interfaz()

    def  boton_Registrar_Regimen(self):
        self.master.destroy()
        root = Tk()
        from Principal_Admin import Principal_Admin
        Principal_Admin(root)
        print("boton_Registrar_Regimen")

    def  boton_Atras(self):
        self.master.destroy()
        root = Tk()
        from Principal_Admin import Principal_Admin
        Principal_Admin(root)
        print("atras")

    images = []  # Para mantener la imagen creada
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


    # ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame12")
    # window.geometry("376x459")

    def crear_interfaz(self):
        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=459,
            width=376,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            347.0,
            235.0,
            image=self.image_image_1
        )

        self.create_rectangle(
            0.0,
            0.0,
            695.0,
            459.0,
            fill="#446575",
            alpha=.8)

        self.canvas.create_rectangle(
            71.0,
            168.0,
            217.0,
            230.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            70.0,
            275.0,
            216.0,
            343.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            414.0,
            376.0,
            458.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            46.0,
            376.0,
            97.0,
            fill="#000000",
            outline="")

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Registrar_Regimen,
            relief="flat"
        )
        self.button_1.place(
            x=189.0,
            y=414.0,
            width=190.0,
            height=43.0
        )

        self.button_image_atras = PhotoImage(
            file=self.relative_to_assets("button_atras.png"))
        self.button_atras = Button(
            image=self.button_image_atras,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Atras,
            relief="flat"
        )
        self.button_atras.place(
            x=0,
            y=414.0,
            width=190.0,
            height=51.0
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            188.5,
            326.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=80.0,
            y=310.0,
            width=217.0,
            height=31.0
        )

        self.canvas.create_text(
            75.0,
            283.0,
            anchor="nw",
            text="Escribir Régimen",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            189.5,
            213.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=80.0,
            y=197.0,
            width=219.0,
            height=31.0
        )

        self.canvas.create_text(
            84.0,
            175.0,
            anchor="nw",
            text="ID del Régimen",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_text(
            43.0,
            60.0,
            anchor="nw",
            text="Registrar Régimen Fiscal",
            fill="#FFFFFF",
            font=("WorkSansRoman Bold", 20 * -1)
        )

        self.master.geometry("376x459")
        self.master.configure(bg="#FFFFFF")
        self.master.resizable(False,False)

    def relative_to_assets(self, path: str) -> Path:
        assets_path = Path(__file__).parent / "assets" / "frame12"
        return assets_path / path
    
if __name__ == "__main__":
    window = Tk()
    app = RegistrarRegimen(window)
    window.mainloop()