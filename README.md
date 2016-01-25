# PyDoctor
Software para el manejo de estudios jurídicos y oficinas judiciales

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
Descargar el instalador desde [descarga windows](http://www.web2py.com/examples/static/web2py_win.zip) o [descarga mac](http://www.web2py.com/examples/static/web2py_osx.zip), descomprimirlo usando Winzip o similar y cliquear en web2py.exe (windows) o web2py.app (osx). 


#### En linux:
clonar usando 
> git clone https://github.com/web2py/web2py.git

### 2. Instalar pyDoctor
en el directorio: 
> *Directorio web2py*/applications

descargue y descomprima el archivo: [zip pydoctor](https://github.com/UniversidadDelEste/PyDoctor/archive/master.zip)

### 3. Ejecutar pyDoctor
Ejecute web2py:
> python.exe web2py.py

Abra el navegador de internet e ingrese el link http://127.0.0.1:8000/PyDoctor/default/index

¡Que lo disfrute!
