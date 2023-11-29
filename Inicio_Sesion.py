from tkinter import Entry, Tk, Canvas, Button, PhotoImage, Toplevel, messagebox
from PIL import Image, ImageTk
from pathlib import Path


class IniciarSesion:
    def __init__(self, master):
        self.master = master
        self.images = []
        self.canvas = None
        self.crear_interfaz()

    def boton_Iniciar_Sesion(self):
        users=["David","Davniel","Julian","Ian","Ivan"]
        password="1234"
        texto = self.entry_2.get()

        if texto in users:
            if(self.entry_1.get() == password):
                self.master.destroy()
                root = Tk()
                from Principal_Agente import PrincipalAgente
                PrincipalAgente(root)
            else:
             messagebox.showwarning("Warning", "La contraseña no es correcta")        
        else:
            messagebox.showwarning("Warning", "EL usuario no se encuentra registrado")

    def boton_Iniciar_Sesion_Administrador(self):
        self.master.destroy()
        root = Tk()
        from Inicio_Sesion_Admin import IniciarSesionAdmin
        IniciarSesionAdmin(root)

    def boton_Ver_Contraseña(self):
        # lógica del botón
        if self.entry_1.cget('show') == '*':
            self.entry_1.config(show='')  # Muestra la contraseña
        else:
            self.entry_1.config(show='*')  # Oculta la contraseña
        print("boton_Ver_contraseña")

    images = []
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
            height=604,
            width=771,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Almacena las imágenes como atributos de la instancia
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            385.0,
            302.0,
            image=self.image_image_1
        )

        self.create_rectangle(
            315.0,
            0.0,
            771.0,
            604.0,
            fill="#00796B",
            alpha=.8)

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Iniciar_Sesion_Administrador,
            relief="flat"
        )
        self.button_1.image = self.button_image_1

        self.button_1.place(
            x=397.0,
            y=569.0,
            width=292.0,
            height=35.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Iniciar_Sesion,
            relief="flat"
        )
        self.button_2.place(
            x=448.0,
            y=486.0,
            width=190.0,
            height=35.0
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            543.0,
            441.5,
            image=self.entry_image_1
        )

        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            show='*'
        )
        self.entry_1.image = self.entry_image_1
        self.entry_1.place(
            x=416.0,
            y=421.0,
            width=254.0,
            height=39.0
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            543.0,
            333.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.image = self.entry_image_2
        self.entry_2.place(
            x=415.0,
            y=313.0,
            width=256.0,
            height=39.0
        )

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Ver_Contraseña,
            relief="flat"
        )
        self.button_3.image = self.button_image_3

        self.button_3.place(
            x=642.0,
            y=427.0,
            width=30.0,
            height=30.0
        )

        self.canvas.create_text(
            405.0,
            391.0,
            anchor="nw",
            text="Contraseña ",
            fill="#FFFFFF",
            font=("Inter Medium", 20 * -1)
        )

        self.canvas.create_text(
            405.0,
            283.0,
            anchor="nw",
            text="Usuario",
            fill="#FFFFFF",
            font=("Inter Medium", 20 * -1)
        )

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            542.0,
            151.0,
            image=self.image_image_2
        )

        self.master.geometry("771x604")
        self.master.configure(bg="#FFFFFF")
        self.master.resizable(False,False)

    def relative_to_assets(self, path: str) -> Path:
        assets_path = Path(__file__).parent / "assets" / "frame7"
        return assets_path / path


if __name__ == "__main__":
    window = Tk()
    app = IniciarSesion(window)
    window.mainloop()