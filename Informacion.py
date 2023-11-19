from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from PIL import Image, ImageTk

class ModificarInformacion:
    def __init__(self, master):
        self.master = master
        self.images = []
        self.canvas = None
        self.crear_interfaz()

    def boton_Informacion_Cliente(self):
        # lógica del botón
        print("boton_Informacion_Cliente")

    def boton_Informacion_Emprendedor(self):
        # lógica del botón
        print("boton_Informacion_Emprendedor")

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

    def crear_interfaz(self):
        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=587,
            width=782,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Almacena las imágenes como atributos de la instancia
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            391.0,
            306.0,
            image=self.image_image_1
        )

        self.create_rectangle(46, 36, 735, 551, fill="#00796B", alpha=.8)

        self.create_rectangle(51.0, 187.0, 751.0, 238.0, fill="#000000", outline="")

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            136.0,
            109.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            298.0,
            195.0,
            anchor="nw",
            text="Modificar Información",
            fill="#FFFFFF",
            font=("WorkSansRoman Bold", 20 * -1)
        )

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Informacion_Cliente,
            relief="flat"
        )
        self.button_1.place(
            x=121.0,
            y=259.0,
            width=220.0,
            height=250.0
        )

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Informacion_Emprendedor,
            relief="flat"
        )
        self.button_2.place(
            x=441.0,
            y=259.0,
            width=220.0,
            height=250.0
        )

        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            230.0,
            411.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            550.0,
            411.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            401.0,
            112.0,
            image=self.image_image_5
        )

    def relative_to_assets(self, path: str) -> Path:
        assets_path = Path(__file__).parent / "assets" / "frame4"
        return assets_path / path

if __name__ == "__main__":
    window = Tk()
    window.geometry("782x587")
    window.configure(bg="#FFFFFF")
    window.resizable(False, False)
    # Crea una instancia de ModificarInformacion
    app = ModificarInformacion(window)

    window.mainloop()
