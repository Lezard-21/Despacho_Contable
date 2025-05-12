from pathlib import Path




# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import INSERT, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, ttk
from PIL import Image, ImageTk
import operaciones_json
class VerAgentes:

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

    def  boton_Atras(self):
        self.master.destroy()
        root = Tk()
        from Principal_Admin import Principal_Admin
        Principal_Admin(root)
        print("boton_Atras")

    def  boton_Cargar_Agente(self):
        #logica del boton
        agentes= operaciones_json.read_json("Agente.json")
        self.entry_1.insert(INSERT,agentes)
        print("boton_Cargar_Agente")
    
    def cargar_datos(self, treeview, datos):
        for i in treeview.get_children():
            treeview.delete(i)

        claves = list(datos.keys())

        num_filas = len(datos[claves[0]])

        for i in range(num_filas):
            fila = [datos[clave][i] for clave in claves]
            treeview.insert("", "end", values=fila)

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

    # ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame19")
    # window.geometry("782x587")

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
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            391.0,
            306.0,
            image=self.image_image_1
        )

        self.create_rectangle(
            46.0,
            36.0,
            735.0,
            551.0,
            fill="#446575",
            alpha=.8)

        self.canvas.create_rectangle(
            46.0,
            180.0,
            735.0,
            415.0,
            fill="#073131",
            outline="")

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Cargar_Agente,
            relief="flat"
        )
        self.button_1.place(
            x=420.0,
            y=459.0,
            width=219.0,
            height=40.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Atras,
            relief="flat"
        )
        self.button_2.place(
            x=142.0,
            y=459.0,
            width=219.0,
            height=40.0
        )

        # self.entry_image_1 = PhotoImage(
        #     file=self.relative_to_assets("entry_1.png"))
        # self.entry_bg_1 = self.canvas.create_image(
        #     390.5,
        #     297.5,
        #     image=self.entry_image_1
        # )
        # self.entry_1 = Text(
        #     bd=0,
        #     bg="#D9D9D9",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_1.place(
        #     x=153.0,
        #     y=200.0,
        #     width=475.0,
        #     height=193.0
        # )

        datos = operaciones_json.read_json("Agente.json")
        print(datos)

        treeview = ttk.Treeview(self.master)

        if not isinstance(datos, dict):
            print("Error: Los datos no son un diccionario.")
            return

        columnas = list(datos.keys())
        treeview["columns"] = columnas
        treeview["show"] = "headings"  

        for columna in columnas:
            treeview.heading(columna, text=columna)
            treeview.column(columna, width=100, anchor="center")  

        self.cargar_datos(treeview,datos)
        treeview.place(
            x=40.0,
            y=200.0,
            width=700.0,
            height=193.0
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            124.0,
            109.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            391.0,
            110.0,
            image=self.image_image_3
        )

        self.master.geometry("782x587")
        self.master.configure(bg="#FFFFFF")
        self.master.resizable(False,False)

    def relative_to_assets(self, path: str) -> Path:
        assets_path = Path(__file__).parent / "assets" / "frame19"
        return assets_path / path
    
if __name__ == "__main__":
    window = Tk()
    app = VerAgentes(window)
    window.mainloop()
