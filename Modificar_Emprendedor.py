from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import INSERT, IntVar, Radiobutton, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import operaciones_json
from PIL import Image, ImageTk
class ModificarEmprendedor:
    def __init__(self, master):
        self.master = master
        self.images = []
        self.canvas = None
        self.crear_interfaz()
        
    def  boton_Modificar_Emprendedor(self):
        #logica del boton
        texto_1 = self.entry_1.get()
        texto_2 = self.entry_2.get()
        texto_3 = self.entry_3.get()
        texto_4 = self.entry_4.get()
        texto_5 = self.entry_5.get()
        texto_6 = self.entry_6.get("1.0", 'end-1c')
        texto_7 = self.selected_value.get()
        texto_8 = self.entry_8.get()
        texto_9 = self.entry_9.get()
        texto_10 = self.entry_10.get()
        texto_11 = self.entry_11.get()
        operaciones_json.add_to_json('Emprendedor.json', 'Nombre', texto_11)
        operaciones_json.add_to_json('Emprendedor.json', 'Nombre de negocio', texto_10)
        operaciones_json.add_to_json('Emprendedor.json', 'Telefono', texto_8)
        operaciones_json.add_to_json('Emprendedor.json', 'Correo electronico', texto_9)
        operaciones_json.add_to_json('Emprendedor.json', 'RFC', texto_5)
        operaciones_json.add_to_json('Emprendedor.json', 'NSS', texto_2)
        operaciones_json.add_to_json('Emprendedor.json', 'Codigo postal', texto_3)
        operaciones_json.add_to_json('Emprendedor.json', 'Tipo de persona', texto_7)
        operaciones_json.add_to_json('Emprendedor.json', 'Capital inicial', texto_4)
        operaciones_json.add_to_json('Emprendedor.json', 'Observaciones', texto_6)
        
        messagebox.showinfo("Confirmation", "Emprendedor Modificado")
        self.master.destroy()
        root = Tk()
        from Principal_Agente import PrincipalAgente
        PrincipalAgente(root)
        print("boton_Modificar_Emprendedor")

    def  boton_Cargar_Emprendedor(self):
        #logica del boton
        Emprendedor= operaciones_json.read_json("Emprendedor.json")
        self.entry_11.insert(INSERT,Emprendedor["Nombre"])
        self.entry_10.insert(INSERT,Emprendedor["Nombre de negocio"])
        self.entry_8.insert(INSERT,Emprendedor["Telefono"])
        self.entry_9.insert(INSERT,Emprendedor["Correo electronico"])
        self.entry_5.insert(INSERT,Emprendedor["RFC"])
        self.entry_2.insert(INSERT,Emprendedor["NSS"])
        self.entry_3.insert(INSERT,Emprendedor["Codigo postal"])

        if(Emprendedor["Tipo de persona"]=="Productor"):self.selected_value.set("Productor")
        if(Emprendedor["Tipo de persona"]=="Marketing"):self.selected_value.set("Marketing")
        if(Emprendedor["Tipo de persona"]=="Equipo de trabajo"):self.selected_value.set("Equipo de trabajo")

        self.entry_4.insert(INSERT,Emprendedor["Capital inicial"])
        self.entry_6.insert(INSERT,Emprendedor["Observaciones"])
        messagebox.showinfo("Confirmation", "Emprendedor cargado")
        print("boton_Cargar_Emprendedor")

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
    # ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame15")


    # def relative_to_assets(path: str) -> Path:
    #     return ASSETS_PATH / Path(path)
    # window.geometry("989x771")

    def crear_interfaz(self):
        self.canvas = Canvas(
            self.master,
            bg="#FFFFFF",
            height=771,
            width=989,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            494.0,
            456.0,
            image=self.image_image_1
        )

        self.create_rectangle(
            0.0,
            0.0,
            989.0,
            912.0,
            fill="#00796B",
            alpha=0.8
        )

        self.canvas.create_rectangle(
            15.0,
            45.0,
            1020.0,
            96.0,
            fill="#000000",
            outline=""
        )

        self.canvas.create_text(
            792.0,
            44.0,
            anchor="nw",
            text="Emprendedor",
            fill="#FFFFFF",
            font=("WorkSansRoman Bold", 20 * -1)
        )

        self.canvas.create_text(
            92.0,
            45.0,
            anchor="nw",
            text="Modificar Información",
            fill="#FFFFFF",
            font=("Inter Bold", 20 * -1)
        )

        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            768.0,
            63.0,
            image=self.image_image_2
        )

        self.canvas.create_rectangle(
            90.0,
            122.0,
            627.0,
            191.0,
            fill="#073131",
            outline=""
        )

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Cargar_Emprendedor,
            relief="flat"
        )
        self.button_1.place(
            x=412.0,
            y=152.0,
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
            y=720.0,
            width=190.0,
            height=51.0
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            218.0,
            167.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=108.0,
            y=152.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            104.0,
            122.0,
            anchor="nw",
            text="Id Emprendedor",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            387.0,
            208.0,
            428.0,
            267.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            387.0,
            387.0,
            503.0,
            446.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            387.0,
            479.0,
            503.0,
            538.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            387.0,
            297.0,
            428.0,
            356.0,
            fill="#073131",
            outline=""
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            507.0,
            341.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=397.0,
            y=326.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            390.0,
            296.0,
            anchor="nw",
            text="NSS",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            507.0,
            431.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=397.0,
            y=416.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            390.0,
            388.0,
            anchor="nw",
            text="Código postal",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            507.0,
            523.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=397.0,
            y=508.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            390.0,
            478.0,
            anchor="nw",
            text="Capital Inicial",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            507.0,
            252.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=397.0,
            y=237.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            390.0,
            207.0,
            anchor="nw",
            text="RFC",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            98.0,
            378.0,
            339.0,
            631.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_text(
            153.0,
            530.0,
            anchor="nw",
            text="Equipo de Trabajo",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            153.0,
            480.0,
            anchor="nw",
            text="Marketing",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_text(
            153.0,
            430.0,
            anchor="nw",
            text="Productor",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        self.canvas.create_rectangle(
            677.0,
            380.0,
            926.0,
            619.0,
            fill="#073131",
            outline=""
        )

        self.entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            801.5,
            509.0,
            image=self.entry_image_6
        )
        self.entry_6 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=694.0,
            y=410.0,
            width=215.0,
            height=196.0
        )

        self.canvas.create_text(
            689.0,
            380.0,
            anchor="nw",
            text="Observaciones",
            fill="#FFFFFF",
            font=("Inter", 16 * -1)
        )

        # self.canvas.create_rectangle(
        #     106.0,
        #     487.0,
        #     137.0,
        #     513.0,
        #     fill="#D9D9D9",
        #     outline=""
        # )

        # self.canvas.create_rectangle(
        #     106.0,
        #     536.0,
        #     137.0,
        #     562.0,
        #     fill="#D9D9D9",
        #     outline=""
        # )

        # self.canvas.create_rectangle(
        #     107.0,
        #     585.0,
        #     138.0,
        #     611.0,
        #     fill="#D9D9D9",
        #     outline=""
        # )

        # Crea una variable para almacenar el valor seleccionado
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
        self.radio1.place(x=106, y=430, width=30.0, height=30.0)
        self.radio2.place(x=106, y=480, width=30.0, height=30.0)
        self.radio3.place(x=107, y=530, width=30.0, height=30.0)

        ############

        # self.entry_image_7 = PhotoImage(file=self.relative_to_assets("entry_7.png"))
        # self.entry_bg_7 = self.canvas.create_image(
        #     218.0,
        #     433.0,
        #     image=self.entry_image_7
        # )
        # self.entry_7 = Entry(
        #     bd=0,
        #     bg="#D9D9D9",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_7.place(
        #     x=108.0,
        #     y=418.0,
        #     width=220.0,
        #     height=28.0
        # )

        self.canvas.create_text(
            104.0,
            388.0,
            anchor="nw",
            text="Tipo de Persona",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.canvas.create_rectangle(
            0.0,
            720.0,
            989.0,
            771.0,
            fill="#000000",
            outline=""
        )

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Modificar_Emprendedor,
            relief="flat"
        )
        self.button_2.place(
            x=799.0,
            y=720.0,
            width=190.0,
            height=51.0
        )

        self.canvas.create_rectangle(
            95.0,
            208.0,
            248.0,
            267.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            682.0,
            298.0,
            840.0,
            357.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            682.0,
            207.0,
            758.0,
            266.0,
            fill="#073131",
            outline=""
        )

        self.canvas.create_rectangle(
            95.0,
            297.0,
            258.0,
            356.0,
            fill="#073131",
            outline=""
        )

        self.entry_image_8 = PhotoImage(file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            802.0,
            251.0,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_8.place(
            x=692.0,
            y=236.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            688.0,
            207.0,
            anchor="nw",
            text="Teléfono",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_9 = PhotoImage(file=self.relative_to_assets("entry_9.png"))
        self.entry_bg_9 = self.canvas.create_image(
            802.0,
            341.0,
            image=self.entry_image_9
        )
        self.entry_9 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_9.place(
            x=692.0,
            y=326.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            688.0,
            296.0,
            anchor="nw",
            text="Correo Electrónico",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_10 = PhotoImage(file=self.relative_to_assets("entry_10.png"))
        self.entry_bg_10 = self.canvas.create_image(
            215.0,
            342.0,
            image=self.entry_image_10
        )
        self.entry_10 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
        )
        self.entry_10.place(
            x=105.0,
            y=327.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            101.0,
            297.0,
            anchor="nw",
            text="Nombre de negocio",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_11 = PhotoImage(
            file=self.relative_to_assets("entry_11.png"))
        self.entry_bg_11 = self.canvas.create_image(
            215.0,
            252.0,
            image=self.entry_image_11
        )
        self.entry_11 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_11.place(
            x=105.0,
            y=237.0,
            width=220.0,
            height=28.0
        )

        self.canvas.create_text(
            101.0,
            207.0,
            anchor="nw",
            text="Nombre completo",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )
        
        self.master.geometry("989x771")
        self.master.configure(bg="#FFFFFF")
        self.master.resizable(False,False)

    def relative_to_assets(self, path: str) -> Path:
        assets_path = Path(__file__).parent / "assets" / "frame15"
        return assets_path / path
    
if __name__ == "__main__":
    window = Tk()
    window.geometry("989x771")
    window.configure(bg="#FFFFFF")
    window.resizable(False, False)
    # Crea una instancia de ModificarAgente
    app = ModificarEmprendedor(window)

    window.mainloop()

