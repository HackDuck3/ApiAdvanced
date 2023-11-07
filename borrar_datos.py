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

nombre_campo = input('Escribe el nombre de un campo del que quieres borrar la fila entera: ')
valorCampo = input('Cual es el valor del campo?')

response = supabase.table(tabla).select("*").eq(nombre_campo, valorCampo).execute()
datos_filtrados = list(json.loads(response.model_dump_json())["data"])
print(datos_filtrados)

borrar_id = input('Selecciona el id que quieres borrar: ')

if tabla == "users":
    response = supabase.from_('events').update({'user_id': None}).match({'user_id': borrar_id}).execute()
    response = supabase.from_('comments').update({'user_id': None}).match({'user_id': borrar_id}).execute()
    time.sleep(1.5)
elif tabla == "tag":
    response = supabase.from_('events').update({'tag_id': None}).match({'tag_id': borrar_id}).execute()
    response = supabase.from_('calendars').update({'tag_id': None}).match({'tag_id': borrar_id}).execute()
    time.sleep(1.5)
elif tabla == "events":
    response = supabase.from_('comments').update({'event_id': None}).match({'event_id': borrar_id}).execute()
    response = supabase.from_('calendars').update({'event_id': None}).match({'event_id': borrar_id}).execute()
    time.sleep(1.5)
elif tabla == "calendars":
    response = supabase.from_('users').update({'calendar_id': None}).match({'calendar_id': borrar_id}).execute()
    time.sleep(1.5)

    
response = supabase.table(tabla).delete().eq(campos[0], borrar_id).execute()