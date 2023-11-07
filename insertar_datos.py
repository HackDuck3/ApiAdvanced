from supabase import create_client, Client
import json

buscando = True
patata = True

url = "https://secxumjiywgzbfdwafsc.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNlY3h1bWppeXdnemJmZHdhZnNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY1MDc4MjgsImV4cCI6MjAxMjA4MzgyOH0.wJUWAsPsIVZoba2OSRAPXUJmexJRjz0t7dSyyxPPDmw"

supabase = create_client(url ,key)

listaTablas = ["tag", "events", "calendars", "comments",  "users"]

while buscando:
    tabla = input('En que tabla quieres introducir los datos? \n - users \n - events \n - calendars \n - comments \n - tag \n')
    for campoTabla in listaTablas:
        
        if tabla.lower() == campoTabla:
            buscando = False

    if buscando != False:
        print("No se encontro la tabla, corrige si esta mal escrito")

response = supabase.table(tabla).select("*").execute()

datos = {}

while patata:
    for campo in list(json.loads(response.model_dump_json())["data"][0].keys()):
        valor = input(f"Ingrese el valor para {campo}: ")
        datos[campo] = valor if valor != "" else None
        print(datos[campo])
    try:
        print(datos)
        response = supabase.table(tabla).insert([datos]).execute()
        patata = False
    except:
        print("Los datos son invalidos")