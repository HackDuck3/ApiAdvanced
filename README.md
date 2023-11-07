# ApiUsuarioBasica
Esto es un repositorio de unos ejercicios de servicios y procesos

# Supabase Client - Documentación

Este repositorio contiene scripts de Python que interactúan con la API de Supabase para realizar operaciones básicas en tablas específicas.

## Requisitos

Antes de ejecutar los scripts, asegúrate de tener instalado Python y la biblioteca `supabase`. Puedes instalar la biblioteca usando `pip`:

```bash
pip install supabase
```
## Configuración

Antes de ejecutar cualquier script, asegúrate de proporcionar la URL y la clave de la API de tu instancia de Supabase en el código. Estos valores se utilizan para autenticar las solicitudes a la API.

```python
from supabase import create_client

url = "https://secxumjiywgzbfdwafsc.supabase.co"
key = "TU_CLAVE_DE_API_AQUI"
supabase = create_client(url, key)
```
## Scripts Disponibles

### 1. Seleccionar datos de una tabla
El siguiente script permite seleccionar todos los registros de una tabla específica y mostrarlos por consola.

```python
tabla = input('¿Qué tabla quieres ver? ')
response = supabase.table(tabla).select('*').execute()
print(response)
```

### 2. Eliminar un registro por ID
Este script solicitará al usuario el nombre del campo ID y el valor correspondiente para eliminar un registro específico de la tabla seleccionada.

```python
nombre_campo = input('Escribe el nombre de un campo del que quieres borrar la fila entera: ')
valorCampo = input('¿Cuál es el valor del campo?')
response = supabase.table(tabla).delete().eq(nombre_campo, valorCampo).execute()
```
### 3. Actualizar un campo específico por ID
Este script permite actualizar un campo específico de un registro en la tabla seleccionada. Solicitará al usuario el nombre del campo ID, el valor correspondiente y el nombre del campo que se desea actualizar junto con su nuevo valor.

```python
idName = input("Escribe el nombre del campo ID: ")
idNumber = int(input("Escribe la ID: "))
camposelect = input("Escribe el nombre del campo: ")
valueinsert = input("Inserta el valor que deseas insertar: ")

response = supabase.table(tabla).update({camposelect: valueinsert}).eq(idName, idNumber).execute()
```

Recuerda que estos son ejemplos básicos y que puedes personalizarlos según tus necesidades específicas. Para más detalles sobre las operaciones disponibles y las opciones de la API de Supabase, consulta la documentación oficial de Supabase.

¡Espero que esta documentación te sea útil!
