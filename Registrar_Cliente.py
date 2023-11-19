from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk

class RegistrarCliente:

    def __init__(self, master):
        self.master = master
        self.images = []
        self.canvas = None
        self.crear_interfaz()

    def boton_Registrar_Cliente(self):
        #logica del boton
        print("boton_Registrar_Cliente")

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


    # ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame9")
    # window.geometry("695x581")

    def crear_interfaz(self):
        self.canvas = Canvas(
        master=self.master,
        bg="#FFFFFF",
        height=581,
        width=695,
        bd=0,
        highlightthickness=0,
        relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            347.0,
            290.0,
            image=self.image_image_1
        )

        self.create_rectangle(
            0.0,
            0.0,
            695.0,
            581.0,
            fill="#00796B",
            alpha=.8)

        self.canvas.create_rectangle(
            90.0,
            91.0,
            243.0,
            150.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            365.0,
            91.0,
            406.0,
            150.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            90.0,
            361.0,
            248.0,
            420.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            90.0,
            272.0,
            166.0,
            331.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            368.0,
            360.0,
            447.0,
            419.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            365.0,
            270.0,
            481.0,
            329.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            90.0,
            180.0,
            253.0,
            239.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            365.0,
            180.0,
            406.0,
            239.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            227.0,
            449.0,
            358.0,
            508.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            530.0,
            695.0,
            581.0,
            fill="#000000",
            outline="")

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Registrar_Cliente,
            relief="flat"
        )
        self.button_1.place(
            x=517.0,
            y=530.0,
            width=178.0,
            height=51.0
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            210.0,
            315.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=100.0,
            y=300.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            96.0,
            271.0,
            anchor="nw",
            text="Teléfono",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            210.0,
            405.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=100.0,
            y=390.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            96.0,
            360.0,
            anchor="nw",
            text="Correo Electrónico",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            210.0,
            225.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=100.0,
            y=210.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            96.0,
            180.0,
            anchor="nw",
            text="Nombre de negocio",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            485.0,
            224.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=375.0,
            y=209.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            368.0,
            179.0,
            anchor="nw",
            text="NSS",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            485.0,
            314.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=375.0,
            y=299.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            368.0,
            271.0,
            anchor="nw",
            text="Código postal",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_6 = PhotoImage(
            file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            485.0,
            135.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=375.0,
            y=120.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            368.0,
            90.0,
            anchor="nw",
            text="RFC",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_7 = PhotoImage(
            file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            210.0,
            135.0,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_7.place(
            x=100.0,
            y=120.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            96.0,
            90.0,
            anchor="nw",
            text="Nombre completo",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_8 = PhotoImage(
            file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            347.0,
            493.0,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_8.place(
            x=237.0,
            y=478.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            233.0,
            448.0,
            anchor="nw",
            text="Régimen Fiscal",
            fill="#FFFFFF",
            font=("WorkSansRoman Medium", 16 * -1)
        )

        self.entry_image_9 = PhotoImage(
            file=self.relative_to_assets("entry_9.png"))
        self.entry_bg_9 = self.canvas.create_image(
            486.5,
            404.5,
            image=self.entry_image_9
        )
        self.entry_9 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_9.place(
            x=378.0,
            y=390.0,
            width=217.0,
            height=27.0
        )

        self.canvas.create_text(
            371.0,
            360.0,
            anchor="nw",
            text="Dirección",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            0.0,
            24.0,
            695.0,
            75.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            92.0,
            38.0,
            anchor="nw",
            text="Registrar Cliente",
            fill="#FFFFFF",
            font=("WorkSansRoman Bold", 20 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            658.0,
            555.0,
            image=self.image_image_2
        )

    def relative_to_assets(self, path: str) -> Path:
                    assets_path = Path(__file__).parent / "assets" / "frame9"
                    return assets_path / path
    
if __name__ == "__main__":
    window = Tk()
    window.geometry("695x581")
    window.configure(bg="#FFFFFF")
    window.resizable(False,False)
    app = RegistrarCliente(window)
    window.mainloop()