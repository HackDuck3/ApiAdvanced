from supabase import create_client, Client
import json
import time

buscando = True
patata = True

url = "https://secxumjiywgzbfdwafsc.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNlY3h1bWppeXdnemJmZHdhZnNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY1MDc4MjgsImV4cCI6MjAxMjA4MzgyOH0.wJUWAsPsIVZoba2OSRAPXUJmexJRjz0t7dSyyxPPDmw"

supabase = create_client(url ,key)

listaTablas = ["tag", "events", "calendars", "comments",  "users"]
listaForanea = ["user_id", "tag_id", "calendar_id", "event_id", "comment_id"]

#Esta preguntando al usuario y buscando el nombre de la tabla
while buscando:
    tabla = input('En que tabla quieres introducir los datos? \n - users \n - events \n - calendars \n - comments \n - tag \n')
    for campoTabla in listaTablas:
        #Filtra el nombre que ha escrito el usuario
        if tabla.lower() == campoTabla:
            buscando = False

    if buscando != False:
        print("No se encontro la tabla, corrige si esta mal escrito")

response = supabase.table(tabla).select("*").execute()


campos = list(json.loads(response.model_dump_json())["data"][0].keys())
campoIndividual = ""
for x in range(len(campos)):
    campoIndividual += "-"+campos[x]+"\n"

print('Esta es la lista de los campos.')
print(campoIndividual)
