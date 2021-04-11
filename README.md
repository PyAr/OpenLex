# OpenLex
Software para el manejo de estudios jurídicos y oficinas judiciales

## Tutorial y demostración

<a href="http://www.youtube.com/watch?feature=player_embedded&v=GK1-XE2Nxdc
" target="_blank"><img src="http://img.youtube.com/vi/GK1-XE2Nxdc/0.jpg" 
alt="tutorial y demostración" width="480" height="360" border="10" /></a>

## Características de nuestra propuesta 
### Características técnicas
* Aplicación basada en el uso de software libre
* Licenciamiento GNU-GPL. 
* Acceso a la aplicación a través de un navegador de Internet: Mozzilla Firefox, Opera, Safary, Ephyfany, Internet Explorer, etc. 
* Uso de patrones y frameworks de trabajo para el desarrollo; en particular Web2Py. 
* Simplicidad para la traducción a otros idiomas.

### Ventajas para el usuario final 
* Garantía de disponibilidad de la información, independientemente de la plataforma del equipo cliente (Linux, Windows, Macintosh, etc). 
* Licenciamiento GNU-GPL: libertad de copia, modificación, mejora del código fuente. 
* Posibilidad de conexión a dispositivos móviles, pudiendo enviar y recibir datos, desde y hacía la aplicación instalada y configurada en forma local. 
* Cantidad ilimitada de usuarios autorizados a acceder al sistema; el administrador del sistema es quien crea los usuarios y define el rol que cumple cada una de las personas. 
* Acceso a la base de datos a través de permisos asignados desde la misma aplicación, pudiendo consultar los datos desde cualquier PC que tenga conexión a Internet y un navegador disponible. 
* Creación de una comunidad de usuarios de la aplicación de manera que la interacción entre quienes la utilizan, permita el crecimiento de la misma. 
* Reutilización de la información cargada en forma local, para poder ser vista a través de Internet sin la necesidad de volver a cargarla. 
* Acceso en todo momento al código fuente de la aplicación, lo que deviene en una mayor transparencia en el uso de las herramientas informáticas. 
* Creación de una comunidad de usuarios de la aplicación, para que participen del desarrollo, como también de las futuras modificaciones que sean necesarias. 

## Módulos incluidos
* Contactos de cada usuario, incluyendo personas físicas y jurídicas
* Listado de juzgados y oficinas judiciales
* Agenda de tareas, vinculadas a las causas
* Seguimiento de expedientes, con carga específica de:
   - Justiciables vinculados a la causa
   - Agenda propia de la causa
   - Procesamiento de los textos judiciales y extrajudiciales.

## Instalación y ejecución
### 1. Instalación de web2py:
#### En windows o mac: 
Descargar el instalador desde [descarga windows](https://mdipierro.pythonanywhere.com/examples/static/web2py_win_py37.zip) o [descarga mac](https://mdipierro.pythonanywhere.com/examples/static/web2py_osx_py37.zip), descomprimirlo usando Winzip o similar y cliquear en web2py.exe (windows) o web2py.app (osx). 


#### En linux:
clonar usando 
```
git clone --recursive https://github.com/web2py/web2py.git
```

### 2. Instalar OpenLex
en el directorio: 
 *Directorio web2py*/applications

descargue y descomprima el archivo: [zip OpenLex](https://github.com/PyAr/OpenLex/archive/master.zip)

o bien clone en el subdirectorio applications
```
git clone https://github.com/PyAr/OpenLex.git
```

### 3. Ejecutar OpenLex
Ejecute web2py:
```
python.exe web2py.py
```
o en Linux
```
python3 web2py.py
```
Abra el navegador de internet e ingrese el link http://127.0.0.1:8000/OpenLex/default/index

puede ingresar como usuarios de prueba

user: egomez@user.com  contraseña: egomez
user: jperez@user.com  contraseña: jperez

Para más información sobre la estructura interna del sistema:
[Descripción sistema](https://github.com/PyAr/OpenLex/blob/master/documents/Descripci%C3%B3n%20sistema.pdf)


¡Que lo disfrute!
