# json_operations.py

import json

def read_json(filename):
  with open(filename, 'r') as f:
      data = json.load(f)
  return data

def add_to_json(filename, key, value):
 data = read_json(filename)
 if key in data:
     # Si la llave ya existe, agrega el nuevo valor a la lista de valores existentes
     if isinstance(data[key], list):
         data[key].append(value)
     else:
         # Si la llave ya existe pero no es una lista, convierte el valor existente en una lista y agrega el nuevo valor
         data[key] = [data[key], value]
 else:
     # Si la llave no existe, crea una nueva entrada con la llave y el valor
     data[key] = value
 with open(filename, 'w') as f:
     json.dump(data, f)

def remove_from_json(filename, key):
  data = read_json(filename)
  if key in data:
      del data[key]
      with open(filename, 'w') as f:
          json.dump(data, f)

def modify_json(filename, key, new_value):
  data = read_json(filename)
  if key in data:
      data[key] = new_value
      with open(filename, 'w') as f:
          json.dump(data, f)
