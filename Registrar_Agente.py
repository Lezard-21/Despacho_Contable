from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from PIL import Image, ImageTk
import operaciones_json
import Validaciones

class RegistrarAgente:

    def __init__(self, master):
        self.master = master
        self.images = []
        self.canvas = None
        self.crear_interfaz()
        self.center_window()

    def center_window(self):
        window_width = self.master.winfo_reqwidth()
        window_height = self.master.winfo_reqheight()
        position_top = int(self.master.winfo_screenheight() / 6 - window_height / 2)
        position_right = int(self.master.winfo_screenwidth() / 3 - window_width / 2)
        self.master.geometry("+{}+{}".format(position_right, position_top))
        
    def  boton_Registrar_Agente(self):
        #logica del boton
        if(self.validar_entrys()):
            texto_1 = self.entry_1.get("1.0", 'end-1c')
            texto_2 = self.entry_2.get()
            texto_3 = self.entry_3.get()
            texto_4 = self.entry_4.get()
            texto_5 = self.entry_5.get()
            texto_6 = self.entry_6.get()

            operaciones_json.add_to_json('Agente.json', 'Nombre', texto_4)
            operaciones_json.add_to_json('Agente.json', 'Nombre de usuario', texto_3)
            operaciones_json.add_to_json('Agente.json', 'Contraseña', texto_2)
            operaciones_json.add_to_json('Agente.json', 'RFC', texto_6)
            operaciones_json.add_to_json('Agente.json', 'NSS', texto_5)
            operaciones_json.add_to_json('Agente.json', 'Observaciones', texto_1)
            messagebox.showinfo("Confirmation", "Agente agregado")
            
            self.master.destroy()
            root = Tk()
            from Principal_Admin import Principal_Admin
            Principal_Admin(root)
        print("boton_Registrar_Agente")
    
    def validar_entrys(self):
        if(not Validaciones.validar_rfc(self.entry_6)):
            return False
        if(not Validaciones.validar_nombre(self.entry_3)):
            return False
        if(not Validaciones.validar_nombre(self.entry_4)):
            return False
        if(not Validaciones.validar_NSS(self.entry_5)):
            return False
        return True
    
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

    def crear_interfaz(self):
        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=599,
            width=717,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            358.0,
            274.0,
            image=self.image_image_1
        )

        self.create_rectangle(
            0.0,
            0.0,
            717.0,
            552.0,
            fill="#446575",
            alpha=.8)

        self.canvas.create_rectangle(
            367.0,
            105.0,
            663.0,
            511.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            25.0,
            717.0,
            76.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            548.0,
            717.0,
            599.0,
            fill="#000000",
            outline="")

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Registrar_Agente,
            relief="flat"
        )
        self.button_1.place(
            x=527.0,
            y=548.0,
            width=190.0,
            height=51.0
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
            y=548.0,
            width=190.0,
            height=51.0
        )

        self.canvas.create_text(
            381.0,
            105.0,
            anchor="nw",
            text="Observaciones",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            92.0,
            39.0,
            anchor="nw",
            text="Registrar Agente",
            fill="#FFFFFF",
            font=("WorkSansRoman Bold", 20 * -1)
        )

        self.canvas.create_rectangle(
            55.0,
            94.0,
            208.0,
            153.0,
            fill="#073131",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            515.0,
            324.5,
            image=self.entry_image_1
        )
        self.entry_1 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=385.0,
            y=156.0,
            width=260.0,
            height=335.0
        )

        self.canvas.create_rectangle(
            55.0,
            275.0,
            156.0,
            334.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            55.0,
            183.0,
            218.0,
            242.0,
            fill="#073131",
            outline="")

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            175.0,
            318.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=65.0,
            y=303.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            61.0,
            274.0,
            anchor="nw",
            text="Contraseña",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            175.0,
            228.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=65.0,
            y=213.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            61.0,
            183.0,
            anchor="nw",
            text="Nombre de usuario",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            175.0,
            138.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=65.0,
            y=123.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            61.0,
            93.0,
            anchor="nw",
            text="Nombre completo",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            55.0,
            363.0,
            96.0,
            422.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            55.0,
            452.0,
            96.0,
            511.0,
            fill="#073131",
            outline="")

        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            175.0,
            496.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=65.0,
            y=481.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            58.0,
            451.0,
            anchor="nw",
            text="NSS",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_6 = PhotoImage(
            file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            175.0,
            407.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=65.0,
            y=392.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            58.0,
            362.0,
            anchor="nw",
            text="RFC",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )


        self.master.geometry("717x599")
        self.master.configure(bg="#FFFFFF")
        self.master.resizable(False,False)

    def relative_to_assets(self, path: str) -> Path:
        assets_path = Path(__file__).parent / "assets" / "frame10"
        return assets_path / path
    
if __name__ == "__main__":
    window = Tk()
    app = RegistrarAgente(window)
    window.mainloop()