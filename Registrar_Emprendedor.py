from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import IntVar, Radiobutton, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from PIL import Image, ImageTk
import Validaciones
import operaciones_json

class RegistrarEmprendedor:

    def __init__(self, master):
        self.master = master
        self.images = []
        self.canvas = None
        self.crear_interfaz()
        self.center_window()

    def center_window(self):
        window_width = self.master.winfo_reqwidth()
        window_height = self.master.winfo_reqheight()
        position_top = int(self.master.winfo_screenheight() / 8 - window_height / 2)
        position_right = int(self.master.winfo_screenwidth() / 3 - window_width / 2)
        self.master.geometry("+{}+{}".format(position_right, position_top))
        
    def  boton_Registrar_Emprendedor(self):
        #logica del boton
        if(self.validar_entrys()):
            texto_1 = self.entry_1.get("1.0", 'end-1c')
            texto_2 = self.entry_2.get()
            texto_3 = self.entry_3.get()
            texto_5 = self.entry_5.get()
            texto_6 = self.entry_6.get()
            texto_4 = self.selected_value.get()
            texto_7 = self.entry_7.get()
            texto_8 = self.entry_8.get()
            texto_9 = self.entry_9.get()
            texto_10 = self.entry_11.get()

            print(texto_10)
            operaciones_json.add_to_json('Emprendedor.json', 'Nombre', texto_6)
            operaciones_json.add_to_json('Emprendedor.json', 'Nombre de negocio', texto_5)
            operaciones_json.add_to_json('Emprendedor.json', 'Telefono', texto_2)
            operaciones_json.add_to_json('Emprendedor.json', 'Correo electronico', texto_3)
            operaciones_json.add_to_json('Emprendedor.json', 'RFC', texto_10)
            operaciones_json.add_to_json('Emprendedor.json', 'NSS', texto_7)
            operaciones_json.add_to_json('Emprendedor.json', 'Codigo postal', texto_8)
            operaciones_json.add_to_json('Emprendedor.json', 'Tipo de persona', texto_4)
            operaciones_json.add_to_json('Emprendedor.json', 'Capital inicial', texto_9)
            operaciones_json.add_to_json('Emprendedor.json', 'Observaciones', texto_1)
            messagebox.showinfo("Confirmation", "Emprendedor agregado")
            
            self.master.destroy()
            root = Tk()
            from Principal_Agente import PrincipalAgente
            PrincipalAgente(root)
        print("Error")

    def validar_entrys(self):
        if(not Validaciones.validar_rfc(self.entry_11)):
            return False
        if(not Validaciones.validar_email(self.entry_3)):
            return False
        if(not Validaciones.validar_nombre(self.entry_6)):
            return False
        if(not Validaciones.validar_numero(self.entry_2)):
            return False
        if(not Validaciones.validar_NSS(self.entry_7)):
            return False
        if(not Validaciones.validar_codigo_postal(self.entry_8)):
            return False
        if(not Validaciones.validar_Capital_inicial(self.entry_9)):
            return False
        return True

    def  boton_Atras(self):
 
        # # Ejemplos de RFC válidos
        # rfc_valido_1 = "XEXT990101NI4"

        # # Validar RFCs
        # resultado_1 = validar_rfc(rfc_valido_1)

        # # Mostrar resultados
        # print(f"¿El RFC '{rfc_valido_1}' es válido? {resultado_1}")

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

    # ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame14")
    # window.geometry("695x771")

    def crear_interfaz(self):
        self.canvas = Canvas(
        self.master,
        bg="#FFFFFF",
        height=771,
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
            385.0,
            image=self.image_image_1
        )

        self.create_rectangle(
            0.0,
            0.0,
            695.0,
            771.0,
            fill="#00796B",
            alpha=0.8)

        self.canvas.create_rectangle(
            0.0,
            720.0,
            695.0,
            771.0,
            fill="#000000",
            outline="")

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Registrar_Emprendedor,
            relief="flat"
        )
        self.button_1.place(
            x=485.0,
            y=720.0,
            width=210.0,
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
            y=720.0,
            width=190.0,
            height=51.0
        )

        self.canvas.create_rectangle(
            92.0,
            440.0,
            333.0,
            681.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            17.0,
            695.0,
            68.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            147.0,
            600.0,
            anchor="nw",
            text="Equipo de Trabajo",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            147.0,
            550.0,
            anchor="nw",
            text="Marketing",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            147.0,
            500.0,
            anchor="nw",
            text="Productor\n",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_rectangle(
            391.0,
            443.0,
            640.0,
            682.0,
            fill="#073131",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            515.5,
            572.0,
            image=self.entry_image_1
        )
        self.entry_1 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=408.0,
            y=473.0,
            width=215.0,
            height=196.0
        )

        self.canvas.create_text(
            403.0,
            443.0,
            anchor="nw",
            text="Observaciones",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            92.0,
            31.0,
            anchor="nw",
            text="Registrar Emprendedor",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        # self.canvas.create_rectangle(
        #     101.0,
        #     543.0,
        #     132.0,
        #     569.0,
        #     fill="#D9D9D9",
        #     outline="")

        # self.canvas.create_rectangle(
        #     101.0,
        #     592.0,
        #     132.0,
        #     618.0,
        #     fill="#D9D9D9",
        #     outline="")

        # self.canvas.create_rectangle(
        #     102.0,
        #     641.0,
        #     133.0,
        #     667.0,
        #     fill="#D9D9D9",
        #     outline="")
        self.selected_value = StringVar()

        self.radio1 = Radiobutton(
           self.master,
           value="Productor",
           variable=self.selected_value,
           indicatoron=0,
           activebackground='green',
           selectcolor='black'
        )
        
        self.radio2 = Radiobutton(
           self.master,
           value="Marketing",
           variable=self.selected_value,
           indicatoron=0,
           activebackground='green',
           selectcolor='black'
        )

        self.radio3 = Radiobutton(
           self.master,
           value="Equipo de trabajo",
           variable=self.selected_value,
           indicatoron=0,
           activebackground='green',
           selectcolor='black'
        )
        # Place radio buttons
        self.radio1.place(x=101, y=500, width=30.0, height=30.0)
        self.radio2.place(x=101, y=550, width=30.0, height=30.0)
        self.radio3.place(x=101, y=600, width=30.0, height=30.0)

        ############
        self.canvas.create_rectangle(
            93.0,
            81.0,
            246.0,
            140.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            93.0,
            351.0,
            251.0,
            410.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            93.0,
            262.0,
            169.0,
            321.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            93.0,
            170.0,
            256.0,
            229.0,
            fill="#073131",
            outline="")

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            213.0,
            305.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=103.0,
            y=290.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            99.0,
            261.0,
            anchor="nw",
            text="Teléfono",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            213.0,
            395.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=103.0,
            y=380.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            99.0,
            350.0,
            anchor="nw",
            text="Correo Electrónico",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            93.0,
            444.0,
            231.0,
            503.0,
            fill="#073131",
            outline="")

        # self.entry_image_4 = PhotoImage(
        #     file=self.relative_to_assets("entry_4.png"))
        # self.entry_bg_4 = self.canvas.create_image(
        #     213.0,
        #     488.0,
        #     image=self.entry_image_4
        # )
        # self.entry_4 = Entry(
        #     bd=0,
        #     bg="#D9D9D9",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_4.place(
        #     x=103.0,
        #     y=473.0,
        #     width=220.0,
        #     height=28.0
        # )
    
        self.canvas.create_text(
            99.0,
            443.0,
            anchor="nw",
            text="Tipo de Persona",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            213.0,
            215.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=103.0,
            y=200.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            99.0,
            170.0,
            anchor="nw",
            text="Nombre de negocio",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_6 = PhotoImage(
            file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            213.0,
            125.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=103.0,
            y=110.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            99.0,
            80.0,
            anchor="nw",
            text="Nombre completo",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            400.0,
            83.0,
            441.0,
            142.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            400.0,
            262.0,
            516.0,
            321.0,
            fill="#073131",
            outline="")

        self.canvas.create_rectangle(
            400.0,
            172.0,
            441.0,
            231.0,
            fill="#073131",
            outline="")

        self.entry_image_7 = PhotoImage(
            file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            520.0,
            216.0,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_7.place(
            x=410.0,
            y=201.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            403.0,
            171.0,
            anchor="nw",
            text="NSS",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_8 = PhotoImage(
            file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            520.0,
            306.0,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_8.place(
            x=410.0,
            y=291.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            403.0,
            263.0,
            anchor="nw",
            text="Código postal",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            400.0,
            350.0,
            516.0,
            409.0,
            fill="#073131",
            outline="")

        self.entry_image_9 = PhotoImage(
            file=self.relative_to_assets("entry_9.png"))
        self.entry_bg_9 = self.canvas.create_image(
            520.0,
            394.0,
            image=self.entry_image_9
        )
        self.entry_9 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_9.place(
            x=410.0,
            y=379.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            405.0,
            350.0,
            anchor="nw",
            text="Capital Inicial",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        # self.entry_image_10 = PhotoImage(
        #     file=self.relative_to_assets("entry_10.png"))
        # self.entry_bg_10 = self.canvas.create_image(
        #     520.0,
        #     127.0,
        #     image=self.entry_image_10
        # )
        # self.entry_10 = Entry(
        #     bd=0,
        #     bg="#D9D9D9",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_10.place(
        #     x=410.0,
        #     y=112.0,
        #     width=22000.0,
        #     height=28.0
        # )

        self.canvas.create_text(
            403.0,
            82.0,
            anchor="nw",
            text="RFC",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            400.0,
            83.0,
            441.0,
            142.0,
            fill="#073131",
            outline="")

        self.entry_image_11 = PhotoImage(
            file=self.relative_to_assets("entry_11.png"))
        self.entry_bg_11 = self.canvas.create_image(
            520.0,
            127.0,
            image=self.entry_image_11
        )
        self.entry_11 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_11.place(
            x=410.0,
            y=112.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            403.0,
            82.0,
            anchor="nw",
            text="RFC",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            667.0,
            746.0,
            image=self.image_image_2
        )

        self.master.geometry("695x771")
        self.master.configure(bg="#FFFFFF")
        self.master.resizable(False,False)

    def relative_to_assets(self, path: str) -> Path:
        assets_path = Path(__file__).parent / "assets" / "frame14"
        return assets_path / path
    
if __name__ == "__main__":
    window = Tk()
    app = RegistrarEmprendedor(window)
    window.mainloop()