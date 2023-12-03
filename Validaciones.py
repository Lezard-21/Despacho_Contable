# validaciones.py

import re
from tkinter import messagebox
from datetime import datetime


def validar_email(email):
   pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
   if re.fullmatch(pattern, email.get()) is not None:
       return True
   else:
       messagebox.showerror(title="Error de formato",message="El formato del emai es incorrecto\nEjemplo de formato correcto: ejemplo@gmail.com")

def validar_numero(num):
   telefono = num.get()
   if len(telefono) != 10:
       messagebox.showerror(title="Error de longitud", message="El número telefónico debe contener exactamente 10 dígitos.")
       return False
   pattern = r'^\d{10}$'
   if re.fullmatch(pattern, telefono) is not None:
       return True
   else:
       messagebox.showerror(title="Error de formato",message="El número telefónico solo puede contener numeros")

def validar_NSS(num):
   nss = num.get()
   if len(nss) != 11:
       messagebox.showerror(title="Error de longitud", message="El NSS debe contener exactamente 11 dígitos.")
       return False
   pattern = r'^\d{11}$'
   if re.fullmatch(pattern, nss) is not None:
       return True
   else:
       messagebox.showerror(title="Error de formato",message="El NSS solo puede contener numeros")

def validar_Capital_inicial(num):
   capital = num.get();
   pattern = r'^\d+$'
   if re.fullmatch(pattern, capital) is not None:
       return True
   else:
       messagebox.showerror(title="Error de formato",message="El capital inicial solo puede contener numeros")

def validar_codigo_postal(num):
   codigo = num.get()
   if len(codigo) != 5:
       messagebox.showerror(title="Error de longitud", message="El código postal debe contener exactamente 5 dígitos.")
       return False
   pattern = r'^\d{5}$'
   if re.fullmatch(pattern, codigo) is not None:
       return True
   else:
       messagebox.showerror(title="Error de formato",message="El codigo postal se compone solo de numeros")

def validar_nombre(texto):
    if (texto.get().isalpha()):
        return True
    messagebox.showerror(title="Error de formato",message="El nombre solo puede contener valores alfabéticos")
    return False

def validar_rfc(valor):
    rfc = valor.get()
    mensaje = "Error el RFC tiene que estar en el siguinete formato: \nPrimer carácter: primera letra del apellido paterno.\nSegundo carácter: primera vocal del apellido paterno.\nTercer carácter: primera letra del apellido materno.\nCuarto carácter: primera letra del nombre.\nQuinto y sexto carácter: primeros números del año de nacimiento.\nSéptimo y octavo: número del mes de nacimiento.\nNoveno y décimo: número del día de nacimiento.\nUndécimo, duodécimo y decimotercero: La homoclave que se compone de letras y números\n\nPara aclarar, la homoclave es un conjunto de tres caracteres que pueden ser letras o números, y son las últimas tres posiciones de la Clave Única de Registro de Población (CURP) en México\nEjemplo 'XEXT990101NI4'"
    print(rfc)
    if len(rfc) != 13:
        messagebox.showerror(title="Error de formato",message=mensaje)
        return False

    # Verificar que el primer caracter sea una letra
    if not rfc[0].isalpha():
        messagebox.showerror(title="Error de formato",message=mensaje)
        return False

    # Verificar que el segundo caracter sea una vocal
    if rfc[1] not in 'AEIOU':
        messagebox.showerror(title="Error de formato",message=mensaje)
        return False

    # Verificar que el tercer caracter sea una letra
    if not rfc[2].isalpha():
        messagebox.showerror(title="Error de formato",message=mensaje)
        return False

    # Verificar que el cuarto caracter sea una letra
    if not rfc[3].isalpha():
        messagebox.showerror(title="Error de formato",message=mensaje)
        return False

    # Verificar que los caracteres quinto y sexto sean dígitos
    if not rfc[4:6].isdigit():
        messagebox.showerror(title="Error de formato",message=mensaje)
        return False

    # Verificar que los caracteres septimo y octavo sean dígitos
    if not rfc[6:8].isdigit():
        messagebox.showerror(title="Error de formato",message=mensaje)
        return False

    # Verificar que los caracteres noveno y decimo sean dígitos
    if not rfc[8:10].isdigit():
        messagebox.showerror(title="Error de formato",message=mensaje)
        return False

    # Verificar que los caracteres onceavo, doceavo y terceavo sean alfanuméricos
    if not rfc[10:13].isalnum():
        messagebox.showerror(title="Error de formato",message=mensaje)
        return False

    # Si todas las verificaciones anteriores son exitosas, el RFC es válido
    return True

def validar_fecha(fecha):
    try:
        datetime.strptime(fecha.get(), "%m/%d/%Y")
        return True
    except ValueError:
        messagebox.showerror(title="Error de formato",message="la fecha tiene que estar en el formato MM/dd/aaaa\nEjemplo: 12/03/2023")
        return False