from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import INSERT, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import operaciones_json
import Validaciones

class ModificarCliente:
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

    def  boton_Modificar_Cliente(self):
        # texto_1 = self.entry_1.get()
        if(self.validar_entrys()):
            texto_2 = self.entry_2.get()
            texto_3 = self.entry_3.get()
            texto_4 = self.entry_4.get()
            texto_5 = self.entry_5.get()
            texto_6 = self.entry_6.get()
            texto_7 = self.entry_7.get()
            texto_8 = self.entry_8.get()
            self.texto_9 = ""
            self.cont = 0
            i = 0
            for regimen in self.regimen:
                if(i==self.entry_9.current()):
                    self.texto_9 = regimen 
                    self.cont = i     
                i = i+1
            # texto_9 = self.entry_9.get()
            texto_10 = self.entry_10.get()
            print("2:"+texto_2)
            print("3:"+texto_3)
            print("4:"+texto_4)
            print("5:"+texto_5)
            print("6:"+texto_6)
            print("7:"+texto_7)
            print("8:"+texto_8)
            print("9:"+self.texto_9)
            print("10:"+texto_10)

            # operaciones_json.modify_json('Cliente.json', 'ID cliente','2233431', '2233431')
            operaciones_json.modify_json('Cliente.json', 'Nombre',self.nombreCliente, texto_8)
            operaciones_json.modify_json('Cliente.json', 'Nombre de negocio',self.negocioCliente, texto_4)
            operaciones_json.modify_json('Cliente.json', 'Telefono',self.telefonoCliente, texto_2)
            operaciones_json.modify_json('Cliente.json', 'Correo electronico',self.correoCliente, texto_3)
            operaciones_json.modify_json('Cliente.json', 'RFC',self.RFCliente, texto_7)
            operaciones_json.modify_json('Cliente.json', 'NSS',self.NSSCliente, texto_5)
            operaciones_json.modify_json('Cliente.json', 'Codigo postal',self.CodigoCliente, texto_6)
            operaciones_json.modify_json('Cliente.json', 'Regimen',self.RegimenCliente, self.texto_9)
            operaciones_json.modify_json('Cliente.json', 'Direccion',self.RegimenCliente, texto_10)
            
            messagebox.showinfo("Confirmation", "Cliente Modificado")

            self.master.destroy()
            root = Tk()
            from Principal_Agente import PrincipalAgente
            PrincipalAgente(root)
        print("boton_Modificar_Cliente")

    def validar_entrys(self):
        if(not Validaciones.validar_rfc(self.entry_7)):
            return False
        if(not Validaciones.validar_email(self.entry_3)):
            return False
        if(not Validaciones.validar_nombre(self.entry_8)):
            return False
        if(not Validaciones.validar_numero(self.entry_2)):
            return False
        if(not Validaciones.validar_NSS(self.entry_5)):
            return False
        if(not Validaciones.validar_codigo_postal(self.entry_6)):
            return False
        return True

    def  boton_Cargar_Cliente(self):

        if self.entry_2['state'] == 'normal':
            self.entry_2.delete(0, 'end')
            self.entry_3.delete(0, 'end')
            self.entry_4.delete(0, 'end')
            self.entry_5.delete(0, 'end')
            self.entry_6.delete(0, 'end')
            self.entry_7.delete(0, 'end')
            self.entry_8.delete(0, 'end')
            self.entry_9.delete(0, 'end')
            self.entry_10.delete(0, 'end')

        self.entry_2['state'] = 'normal'
        self.entry_3['state'] = 'normal'
        self.entry_4['state'] = 'normal'
        self.entry_5['state'] = 'normal'
        self.entry_6['state'] = 'normal'
        self.entry_7['state'] = 'normal'
        self.entry_8['state'] = 'normal'
        self.entry_9['state'] = 'normal'
        self.entry_10['state'] = 'normal'

        print(self.comboValues)
        nombre_buscado = self.nombres[self.entry_1.current()]
        indice = self.comboValues["Nombre"].index(nombre_buscado)
        cliente = {k: v[indice] for k, v in self.comboValues.items()}   

        self.nombreCliente = cliente["Nombre"]
        self.negocioCliente = cliente["Nombre de negocio"]
        self.telefonoCliente = cliente["Telefono"]
        self.correoCliente = cliente["Correo electronico"]
        self.RFCliente = cliente["RFC"]
        self.NSSCliente = cliente["NSS"]
        self.CodigoCliente = cliente["Codigo postal"]
        self.RegimenCliente = cliente["Regimen"]
        self.DireccionCliente = cliente["Direccion"]

        # Cliente= operaciones_json.read_json("Cliente.json")
        self.entry_8.insert(INSERT,cliente["Nombre"])
        self.entry_4.insert(INSERT,cliente["Nombre de negocio"])
        self.entry_2.insert(INSERT,cliente["Telefono"])
        self.entry_3.insert(INSERT,cliente["Correo electronico"])
        self.entry_7.insert(INSERT,cliente["RFC"])
        self.entry_5.insert(INSERT,cliente["NSS"])
        self.entry_6.insert(INSERT,cliente["Codigo postal"])
        self.entry_9.insert(INSERT,cliente["Regimen"])
        self.entry_10.insert(INSERT,cliente["Direccion"])
        
        messagebox.showinfo("Confirmation", "Cliente cargado")
        print("boton_Cargar_Cliente")

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

    # OUTPUT_PATH = Path(__file__).parent
    # ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame13")

    # window.geometry("695x717")

    def crear_interfaz(self):
        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=717,
            width=695,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            347.0,
            395.0,
            image=self.image_image_1
        )

        self.create_rectangle(
            0.0,
            0.0,
            695.0,
            717.0,
            fill="#00796B",
            alpha=.8
        )

        self.canvas.create_rectangle(
            8.0,
            32.0,
            703.0,
            83.0,
            fill="#000000",
            outline=""
        )

        self.canvas.create_text(
            10.0,
            34.0,
            anchor="nw",
            text="Modificar Información",
            fill="#FFFFFF",
            font=("WorkSansRoman Bold", 20 * -1)
        )

        self.canvas.create_text(
            556.0,
            31.0,
            anchor="nw",
            text="Cliente",
            fill="#FFFFFF",
            font=("WorkSansRoman Bold", 20 * -1)
        )

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            526.0,
            52.0,
            image=self.image_image_2
        )

        self.canvas.create_rectangle(
            78.0,
            109.0,
            593.0,
            178.0,
            fill="#073131",
            outline=""
        )

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Cargar_Cliente,
            relief="flat"
        )
        self.button_1.place(
            x=375.0,
            y=139.0,
            width=190.0,
            height=30.0
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
            y=666.0,
            width=190.0,
            height=51.0
        )

        # self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        # self.entry_bg_1 = self.canvas.create_image(
        #     206.0,
        #     154.0,
        #     image=self.entry_image_1
        # )
        # self.entry_1 = Entry(
        #     bd=0,
        #     bg="#D9D9D9",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_1.place(
        #     x=96.0,
        #     y=139.0,
        #     width=220.0,
        #     height=28.0
        # )
        self.comboValues = operaciones_json.read_json("Cliente.json")
        self.nombres = self.comboValues["Nombre"]
        self.RFC = self.comboValues["RFC"]
        cont = 0
        self.values = []
        for nombre in self.nombres:
            print(nombre)
            self.values.append(nombre+"-"+self.RFC[cont])
            cont = cont + 1
        self.entry_1 = Combobox(self.canvas, values=self.values)
        self.entry_1.place(x=96, y=139, width=220, height=28)

        self.canvas.create_text(
            92.0,
            109.0,
            anchor="nw",
            text="Cliente",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            0.0,
            666.0,
            695.0,
            717.0,
            fill="#000000",
            outline=""
        )

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Modificar_Cliente,
            relief="flat"
        )
        self.button_2.place(
            x=505.0,
            y=666.0,
            width=190.0,
            height=51.0
        )

        self.canvas.create_rectangle(
            78.0,
            211.0,
            231.0,
            270.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            353.0,
            211.0,
            394.0,
            270.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            78.0,
            481.0,
            236.0,
            540.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            78.0,
            392.0,
            154.0,
            451.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            356.0,
            480.0,
            435.0,
            539.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            353.0,
            390.0,
            469.0,
            449.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            78.0,
            300.0,
            241.0,
            359.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            353.0,
            300.0,
            394.0,
            359.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            215.0,
            569.0,
            346.0,
            628.0,
            fill="#073131",
            outline=""
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            198.0,
            435.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=88.0,
            y=420.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            84.0,
            391.0,
            anchor="nw",
            text="Teléfono",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            198.0,
            525.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=88.0,
            y=510.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            84.0,
            480.0,
            anchor="nw",
            text="Correo Electrónico",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            198.0,
            345.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=88.0,
            y=330.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            84.0,
            300.0,
            anchor="nw",
            text="Nombre de negocio",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            473.0,
            344.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=363.0,
            y=329.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            356.0,
            299.0,
            anchor="nw",
            text="NSS",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            473.0,
            434.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=363.0,
            y=419.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            356.0,
            391.0,
            anchor="nw",
            text="Código postal",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_7 = PhotoImage(file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            473.0,
            255.0,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_7.place(
            x=363.0,
            y=240.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            356.0,
            210.0,
            anchor="nw",
            text="RFC",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_8 = PhotoImage(file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            198.0,
            255.0,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_8.place(
            x=88.0,
            y=240.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            84.0,
            210.0,
            anchor="nw",
            text="Nombre completo",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        # self.entry_image_9 = PhotoImage(file=self.relative_to_assets("entry_9.png"))
        # self.entry_bg_9 = self.canvas.create_image(
        #     335.0,
        #     613.0,
        #     image=self.entry_image_9
        # )
        # self.entry_9 = Entry(
        #     bd=0,
        #     bg="#D9D9D9",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_9.place(
        #     x=225.0,
        #     y=598.0,
        #     width=220.0,
        #     height=28.0
        # )
        self.comboRegimenValues = operaciones_json.read_json("RegimenFiscal.json")
        self.regimen = self.comboRegimenValues["Regimen"]
        self.idRegimen = self.comboRegimenValues["Id regimen"]
        cont = 0
        self.values = []
        for nombre in self.regimen:
            self.values.append(nombre+"-"+self.idRegimen[cont])
            cont = cont + 1
        self.entry_9 = Combobox(self.canvas, values=self.values)
        self.entry_9.place(x=225, y=598, width=220, height=28)

        self.canvas.create_text(
            221.0,
            568.0,
            anchor="nw",
            text="Régimen Fiscal",
            fill="#FFFFFF",
            font=("WorkSansRoman Medium", 16 * -1)
        )

        self.entry_image_10 = PhotoImage(file=self.relative_to_assets("entry_10.png"))
        self.entry_bg_10 = self.canvas.create_image(
            474.5,
            524.5,
            image=self.entry_image_10
        )
        self.entry_10 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_10.place(
            x=366.0,
            y=510.0,
            width=217.0,
            height=27.0
        )

        self.canvas.create_text(
            359.0,
            480.0,
            anchor="nw",
            text="Dirección",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.master.geometry("695x717")
        self.master.configure(bg="#FFFFFF")
        self.master.resizable(False,False)

        self.entry_2['state'] = 'disabled'
        self.entry_3['state'] = 'disabled'
        self.entry_4['state'] = 'disabled'
        self.entry_5['state'] = 'disabled'
        self.entry_6['state'] = 'disabled'
        self.entry_7['state'] = 'disabled'
        self.entry_8['state'] = 'disabled'
        self.entry_9['state'] = 'disabled'
        self.entry_10['state'] = 'disabled'

    def relative_to_assets(self, path: str) -> Path:
        assets_path = Path(__file__).parent / "assets" / "frame13"
        return assets_path / path

if __name__ == "__main__":
    window = Tk()
    app = ModificarCliente(window)
    window.mainloop()