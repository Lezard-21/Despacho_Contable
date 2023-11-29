from pathlib import Path
from tkinter import INSERT, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import operaciones_json
class ModificarAgente:
    def __init__(self, master):
        self.master = master
        self.images = []
        self.canvas = None
        self.crear_interfaz()

    def boton_Modificar_Agente(self):
        # lógica del botón
        texto_1 = self.entry_1.get()
        texto_2 = self.entry_2.get()
        texto_3 = self.entry_3.get()
        texto_4 = self.entry_4.get("1.0", 'end-1c')
        texto_5 = self.entry_5.get()
        texto_6 = self.entry_6.get()

        operaciones_json.add_to_json('Agente.json', 'Nombre', texto_6)
        operaciones_json.add_to_json('Agente.json', 'Nombre de usuario', texto_2)
        operaciones_json.add_to_json('Agente.json', 'Contraseña', texto_1)
        operaciones_json.add_to_json('Agente.json', 'RFC', texto_5)
        operaciones_json.add_to_json('Agente.json', 'NSS', texto_3)
        operaciones_json.add_to_json('Agente.json', 'Observaciones', texto_4)
        messagebox.showinfo("Confirmation", "Agente Modificado")
        self.master.destroy()
        root = Tk()
        from Principal_Admin import Principal_Admin
        Principal_Admin(root)
        print("boton_Modificar_Agente")

    def boton_Cargar_Agente(self):
        # lógica del botón
        Agente= operaciones_json.read_json("Agente.json")
        self.entry_6.insert(INSERT,Agente["Nombre"])
        self.entry_2.insert(INSERT,Agente["Nombre de usuario"])
        self.entry_1.insert(INSERT,Agente["Contraseña"])
        self.entry_5.insert(INSERT,Agente["RFC"])
        self.entry_3.insert(INSERT,Agente["NSS"])
        self.entry_4.insert(INSERT,Agente["Observaciones"])
        
        messagebox.showinfo("Confirmation", "Agente cargado")
        print("boton_Cargar_Agente")

    def  boton_Atras(self):
        self.master.destroy()
        root = Tk()
        from Principal_Admin import Principal_Admin
        Principal_Admin(root)
        print("atras")
        
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
            height=709,
            width=717,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Almacena las imágenes como atributos de la instancia
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            358.0,
            354.0,
            image=self.image_image_1
        )

        self.create_rectangle(0.0, 0.0, 717.0, 709.0, fill="#446575", alpha=.8)

        self.create_rectangle(0.0, 658.0, 717.0, 709.0, fill="#000000", outline="")

        self.create_rectangle(3.0, 27.0, 720.0, 78.0, fill="#000000", outline="")

        self.create_rectangle(58.0, 134.0, 624.0, 227.0, fill="#073131", outline="")

        self.create_rectangle(388.0, 240.0, 434.0, 300.0, fill="#073131", outline="")

        self.create_rectangle(387.0, 337.0, 433.0, 394.0, fill="#073131", outline="")

        self.create_rectangle(79.0, 331.0, 237.0, 395.0, fill="#073131", outline="")

        self.create_rectangle(81.0, 240.0, 245.0, 300.0, fill="#073131", outline="")

        self.create_rectangle(77.0, 422.0, 186.0, 488.0, fill="#073131", outline="")

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Modificar_Agente,
            relief="flat"
        )
        self.button_1.place(
            x=527.0,
            y=658.0,
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
            y=658.0,
            width=190.0,
            height=51.0
        )

        self.create_rectangle(379.0, 422.0, 630.0, 594.0, fill="#073131", outline="")

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.boton_Cargar_Agente,
            relief="flat"
        )
        self.button_2.place(
            x=411.0,
            y=163.0,
            width=190.0,
            height=36.0
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            197.5,
            471.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=87.0,
            y=454.0,
            width=221.0,
            height=32.0
        )

        self.canvas.create_text(
            86.0,
            428.0,
            anchor="nw",
            text="Contraseña",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            198.5,
            378.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=89.0,
            y=362.0,
            width=219.0,
            height=31.0
        )

        self.canvas.create_text(
            85.0,
            338.0,
            anchor="nw",
            text="Nombre de Usuario",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            505.5,
            378.5,
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
            y=363.0,
            width=217.0,
            height=29.0
        )

        self.canvas.create_text(
            394.0,
            341.0,
            anchor="nw",
            text="NSS",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            505.5,
            517.5,
            image=self.entry_image_4
        )
        self.entry_4 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=397.0,
            y=454.0,
            width=217.0,
            height=125.0
        )

        self.canvas.create_text(
            388.0,
            428.0,
            anchor="nw",
            text="Observaciones",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            505.5,
            286.5,
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
            y=270.0,
            width=217.0,
            height=31.0
        )

        self.canvas.create_text(
            394.0,
            244.0,
            anchor="nw",
            text="RFC\n",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        self.entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            198.5,
            286.5,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=89.0,
            y=270.0,
            width=219.0,
            height=31.0
        )

        self.canvas.create_text(
            83.0,
            244.0,
            anchor="nw",
            text="Nombre completo",
            fill="#FFFFFF",
            font=("WorkSansRoman Regular", 16 * -1)
        )

        # self.entry_image_7 = PhotoImage(file=self.relative_to_assets("entry_7.png"))
        # self.entry_bg_7 = self.canvas.create_image(
        #     198.5,
        #     189.5,
        #     image=self.entry_image_7
        # )
        self.comboValues = operaciones_json.read_json("Agente.json")
        self.nombres = self.comboValues["Nombre"]
        self.entry_7 = Combobox(self.canvas, values=self.nombres)
        self.entry_7.place(x=89, y=173, width=219, height=31)
        self.canvas.create_text(81, 141, anchor="nw", text="Agente", fill="#FFFFFF", font=("WorkSansRoman Regular", 16 * -1))

        self.canvas.create_text(
            92.0,
            39.0,
            anchor="nw",
            text="Modificar Agente",
            fill="#FFFFFF",
            font=("WorkSansRoman Bold", 20 * -1)
        )

        self.master.geometry("717x709")
        self.master.configure(bg="#FFFFFF")
        self.master.resizable(False,False)

    def relative_to_assets(self, path: str) -> Path:
        assets_path = Path(__file__).parent / "assets" / "frame11"
        return assets_path / path

if __name__ == "__main__":
    window = Tk()
    # Crea una instancia de ModificarAgente
    app = ModificarAgente(window)

    window.mainloop()
