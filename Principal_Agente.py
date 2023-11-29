from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Toplevel
from PIL import Image, ImageTk

class PrincipalAgente:
    def __init__(self, master):
        self.master = master
        self.images = []
        self.canvas = None
        self.crear_interfaz()
        

    def boton_Registrar_Cliente(self):
        self.master.destroy()
        root = Tk()
        from Registrar_Cliente import RegistrarCliente
        RegistrarCliente(root)
        print("boton_Registrar_Cliente")

    def boton_Ver_Cliente(self):
        self.master.destroy()
        root = Tk()
        from Ver_Clientes import VerClientes
        VerClientes(root)
        print("boton_Ver_Cliente")


    def boton_Registrar_Emprendedor(self):
        self.master.destroy()
        root = Tk()
        from Registrar_Emprendedor import RegistrarEmprendedor
        RegistrarEmprendedor(root)
        print("boton_Registrar_Emprendedor")


    def boton_Ver_Emprendedores(self):
        self.master.destroy()
        root = Tk()
        from Ver_Emprendedores import VerEmprendedores
        VerEmprendedores(root)
        print("boton_Ver_Emprendedores")


    def boton_cambiar_Cliente_A_Emprendedor(self):
        self.master.destroy()
        root = Tk()
        from Ver_Atenciones import VerAtenciones
        VerAtenciones(root)
        print("boton_cambiar_Cliente_A_Emprendedor")


    def boton_Hacer_Atenciones(self):
        self.master.destroy()
        root = Tk()
        from Atenciones import RegistrarAtenciones
        RegistrarAtenciones(root)
        print("boton_Hacer_Atenciones")


    def boton_cambiar_informacion(self):
        self.master.destroy()
        root = Tk()
        from Informacion import ModificarInformacion 
        ModificarInformacion(root)
        print("boton_Cambiar_informacion")


    def boton_Cerrar_Sesion(self):
        self.master.destroy()
        root = Tk()
        from Inicio_Sesion import IniciarSesion
        IniciarSesion(root)
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

    def crear_interfaz(self):
            self.canvas = Canvas(
                self.master,
                bg="#FFFFFF",
                height=657,
                width=741,
                bd=0,
                highlightthickness=0,
                relief="ridge"
            )
            self.canvas.place(x=0, y=0)

            self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
            self.image_1 = self.canvas.create_image(
                517.0,
                334.0,
                image=self.image_image_1
            )

            self.create_rectangle( 0, 30, 741, 610, fill="#00796B", alpha=.8)

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
                x=0.0,
                y=209.0,
                width=350.0,
                height=100.0
            )

            self.button_image_2 = PhotoImage(
                file=self.relative_to_assets("button_2.png"))
            self.button_2 = Button(
                image=self.button_image_2,
                borderwidth=0,
                highlightthickness=0,
                command=self.boton_Ver_Cliente,
                relief="flat"
            )
            self.button_2.place(
                x=0.0,
                y=334.0,
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
                bg="#00796B"
            )
            self.button_3.place(
                x=567.0,
                y=568.0,
                width=174.0,
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
                bg="#00796B"
            )
            self.button_4.place(
                x=596.0,
                y=53.0,
                width=145.0,
                height=37.0
            )

            self.button_image_5 = PhotoImage(
                file=self.relative_to_assets("button_5.png"))
            self.button_5 = Button(
                image=self.button_image_5,
                borderwidth=0,
                highlightthickness=0,
                command=self.boton_Registrar_Emprendedor,
                relief="flat"
            )
            self.button_5.place(
                x=393.0,
                y=209.0,
                width=350.0,
                height=100.0
            )

            self.button_image_6 = PhotoImage(
                file=self.relative_to_assets("button_6.png"))
            self.button_6 = Button(
                image=self.button_image_6,
                borderwidth=0,
                highlightthickness=0,
                command=self.boton_Ver_Emprendedores,
                relief="flat"
            )
            self.button_6.place(
                x=391.0,
                y=334.0,
                width=350.0,
                height=100.0
            )

            self.image_image_2 = PhotoImage(
                file=self.relative_to_assets("image_2.png"))
            self.image_2 = self.canvas.create_image(
                370.0,
                110.0,
                image=self.image_image_2
            )

            self.button_image_7 = PhotoImage(
                file=self.relative_to_assets("button_7.png"))
            self.button_7 = Button(
                image=self.button_image_7,
                borderwidth=0,
                highlightthickness=0,
                command=self.boton_cambiar_Cliente_A_Emprendedor,
                relief="flat"
            )
            self.button_7.place(
                x=0.0,
                y=461.0,
                width=350.0,
                height=100.0
            )

            self.button_image_8 = PhotoImage(
                file=self.relative_to_assets("button_8.png"))
            self.button_8 = Button(
                image=self.button_image_8,
                borderwidth=0,
                highlightthickness=0,
                command=self.boton_Hacer_Atenciones,
                relief="flat"
            )
            self.button_8.place(
                x=391.0,
                y=461.0,
                width=350.0,
                height=100.0
            )
            self.master.geometry("741x604")
            self.master.configure(bg="#FFFFFF")
            self.master.resizable(False,False)    

    def relative_to_assets(self, path: str) -> Path:
        assets_path = Path(__file__).parent / "assets" / "frame5"
        return assets_path / path

if __name__ == "__main__":
    window = Tk()
    # Crea una instancia de IniciarSesion
    app = PrincipalAgente(window)
    window.mainloop()
