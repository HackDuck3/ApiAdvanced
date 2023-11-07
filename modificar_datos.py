from supabase import create_client
import json

url = "https://secxumjiywgzbfdwafsc.supabase.co/"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNlY3h1bWppeXdnemJmZHdhZnNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY1MDc4MjgsImV4cCI6MjAxMjA4MzgyOH0.wJUWAsPsIVZoba2OSRAPXUJmexJRjz0t7dSyyxPPDmw"

supabase = create_client(url, key)

#Por ejemplo, para listar los datos de una tabla:
table_name = input("Introduce el nombre de la tabla a modificar: \n -tag \n -calendars \n -comments \n -events \n -users \n ")

response = supabase.table(table_name).select("*").execute()

campos = list(json.loads(response.model_dump_json())["data"][0].keys())
campoIndividual = ""
for x in range(len(campos)):
    campoIndividual += "-"+campos[x]+"\n"

print('Esta es la lista de los campos en: '+table_name)
print(campoIndividual)

while True:
    idName = input("Escribe el nombre del campo Id: ")
    if idName is None :
        print(f"'{idName}' no es un campo válido para la tabla. Por favor, ingresa un campo válido.")
        continue

    idNumber = int(input("Escribe la Id: "))
    if idNumber < 0:
        print("La Id debe ser un número entero positivo. Inténtalo de nuevo.")
        continue

    camposelect = input("Escribe el nombre del campo: ")
    if camposelect not in campos:
        print(f"'{camposelect}' no es un campo válido para la tabla. Por favor, ingresa un campo válido.")
        continue

    valueinsert = input("Inserta el valor que deseas insertar: ")

    response = supabase.table(table_name).update({camposelect: valueinsert}).eq(idName, idNumber).execute()