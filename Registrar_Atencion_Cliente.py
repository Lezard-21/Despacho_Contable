from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import Validaciones
from PIL import Image, ImageTk
# import mysql.connector
import operaciones_json
class RegistrarAtencionAgente:

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

    def  boton_Registrar_Atencion_Cliente(self):
        #logica del boton
        if(self.validar_entrys()):
            texto_1 = self.entry_1.get()
            texto_2 = self.entry_2.get()
            texto_3 = self.entry_3.get()
            # texto_4 = self.entry_4.get()
            texto_6 = self.entry_6.get()
            # texto_7 = self.entry_7.get()
            texto_8 = self.entry_8.get()
            texto_9 = self.entry_9.get("1.0", 'end-1c')
            # operaciones_json.add_to_json('Atencion_Cliente.json', 'ID cliente', texto_4)
            operaciones_json.add_to_json('Atencion_Cliente.json', 'Nombre', texto_3)
            operaciones_json.add_to_json('Atencion_Cliente.json', 'Telefono', texto_1)
            operaciones_json.add_to_json('Atencion_Cliente.json', 'Correo electronico', texto_2)
            operaciones_json.add_to_json('Atencion_Cliente.json', 'RFC', texto_6)
            operaciones_json.add_to_json('Atencion_Cliente.json', 'Fecha', texto_8)
            operaciones_json.add_to_json('Atencion_Cliente.json', 'Observaciones', texto_9)
            messagebox.showinfo("Confirmation", "Atención a cliente agregada")
            
            self.master.destroy()
            root = Tk()
            from Principal_Agente import PrincipalAgente
            PrincipalAgente(root)
        print("boton_Registrar_Atencion_Cliente")

    # Valida si el RFC existe en el json cliente
    def validar_Existencia_RFC(self,entry):
        jsonValues = operaciones_json.read_json("Cliente.json")
        buscar = entry.get()
        rfc = jsonValues["RFC"]
        for v in rfc:
            if(v==buscar):
                return True
        messagebox.showerror(title="Error dato no existe",message="El RFC que ingreso no se encuentra registrado")
        return False
    
    def validar_entrys(self):
        if(not self.validar_Existencia_RFC(self.entry_6)):
            return False
        if(not Validaciones.validar_rfc(self.entry_6)):
            return False
        if(not Validaciones.validar_email(self.entry_2)):
            return False
        if(not Validaciones.validar_nombre(self.entry_3)):
            return False
        if(not Validaciones.validar_numero(self.entry_1)):
            return False
        if(not Validaciones.validar_fecha(self.entry_8)):
            return False
        return True
    
    def  boton_Atras(self):
        self.master.destroy()
        root = Tk()
        from Principal_Agente import PrincipalAgente
        PrincipalAgente(root)
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

    # ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame16")

    # window.geometry("695x672")

    def crear_interfaz(self):
        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=672,
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
            336.0,
            image=self.image_image_1
        )

        self.create_rectangle(
            0.0,
            0.0,
            695.0,
            672.0,
            fill="#00796B",
            alpha=0.8)
        
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
            y=621.0,
            width=190.0,
            height=51.0
        )

        self.canvas.create_rectangle(
            0.0,
            621.0,
            695.0,
            672.0,
            fill="#000000",
            outline="")

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Registrar_Atencion_Cliente,
            relief="flat"
        )
        self.button_1.place(
            x=505.0,
            y=621.0,
            width=190.0,
            height=51.0
        )

        self.canvas.create_rectangle(
            0.0,
            17.0,
            695.0,
            68.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            92.0,
            31.0,
            anchor="nw",
            text="Atención a Cliente",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.canvas.create_rectangle(
            400.0,
            178.0,
            558.0,
            237.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            89.0,
            178.0,
            165.0,
            237.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            400.0,
            87.0,
            476.0,
            146.0,
            fill="#073131",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            209.0,
            222.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=99.0,
            y=207.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            95.0,
            177.0,
            anchor="nw",
            text="Teléfono",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            520.0,
            222.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=410.0,
            y=207.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            406.0,
            177.0,
            anchor="nw",
            text="Correo Electrónico",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            520.0,
            132.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=410.0,
            y=117.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            406.0,
            87.0,
            anchor="nw",
            text="Nombre",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        # self.canvas.create_rectangle(
        #     89.0,
        #     88.0,
        #     178.0,
        #     147.0,
        #     fill="#073131",
        #     outline="")

        # self.entry_image_4 = PhotoImage(
        #     file=self.relative_to_assets("entry_4.png"))
        # self.entry_bg_4 = self.canvas.create_image(
        #     209.0,
        #     132.0,
        #     image=self.entry_image_4
        # )
        # self.entry_4 = Entry(
        #     bd=0,
        #     bg="#D9D9D9",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_4.place(
        #     x=99.0,
        #     y=117.0,
        #     width=220.0,
        #     height=28.0
        # )

        # self.canvas.create_text(
        #     95.0,
        #     87.0,
        #     anchor="nw",
        #     text="ID Cliente",
        #     fill="#FFFFFF",
        #     font=("WorkSansRoman Regular", 16 * -1)
        # )

        # self.canvas.create_rectangle(
        #     400.0,
        #     268.0,
        #     441.0,
        #     327.0,
        #     fill="#073131",
        #     outline="")

        # self.entry_image_5 = PhotoImage(
        #     file=self.relative_to_assets("entry_5.png"))
        # self.entry_bg_5 = self.canvas.create_image(
        #     520.0,
        #     312.0,
        #     image=self.entry_image_5
        # )
        # self.entry_5 = Entry(
        #     bd=0,
        #     bg="#D9D9D9",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_5.place(
        #     x=410.0,
        #     y=297.0,
        #     width=220.0,
        #     height=28.0
        # )

        self.canvas.create_text(
            403.0,
            267.0,
            anchor="nw",
            text="RFC",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            400.0,
            268.0,
            441.0,
            327.0,
            fill="#073131",
            outline="")

        self.entry_image_6 = PhotoImage(
            file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            520.0,
            312.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=410.0,
            y=297.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            403.0,
            267.0,
            anchor="nw",
            text="RFC",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            89.0,
            268.0,
            130.0,
            327.0,
            fill="#073131",
            outline="")

        # self.entry_image_7 = PhotoImage(
        #     file=self.relative_to_assets("entry_7.png"))
        # self.entry_bg_7 = self.canvas.create_image(
        #     209.0,
        #     312.0,
        #     image=self.entry_image_7
        # )
        # self.entry_7 = Entry(
        #     bd=0,
        #     bg="#D9D9D9",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_7.place(
        #     x=99.0,
        #     y=297.0,
        #     width=220.0,
        #     height=28.0
        # )

        self.canvas.create_text(
            92.0,
            267.0,
            anchor="nw",
            text="RFC",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            89.0,
            268.0,
            142.0,
            327.0,
            fill="#073131",
            outline="")

        self.entry_image_8 = PhotoImage(
            file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            209.0,
            312.0,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_8.place(
            x=99.0,
            y=297.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            89.0,
            267.0,
            anchor="nw",
            text="Fecha",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            89.0,
            359.0,
            643.0,
            598.0,
            fill="#073131",
            outline="")

        self.entry_image_9 = PhotoImage(
            file=self.relative_to_assets("entry_9.png"))
        self.entry_bg_9 = self.canvas.create_image(
            366.0,
            488.0,
            image=self.entry_image_9
        )
        self.entry_9 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_9.place(
            x=115.0,
            y=389.0,
            width=502.0,
            height=196.0
        )

        self.canvas.create_text(
            116.0,
            359.0,
            anchor="nw",
            text="Observaciones",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.master.geometry("695x672")
        self.master.configure(bg="#FFFFFF")
        self.master.resizable(False,False)

    def relative_to_assets(self, path: str) -> Path:
            assets_path = Path(__file__).parent / "assets" / "frame16"
            return assets_path / path
    
if __name__ == "__main__":
    window = Tk()
    app = RegistrarAtencionAgente(window)
    window.mainloop()
