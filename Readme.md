# Python y Django
## Objetivo
Realizar una aplicación funcional con formulario y almacenamiento de datos en SQLite.

## Video de Faztweb [https://www.youtube.com/watch?v=T1intZyhXDU&list=PLL0TiOXBeDai29Uz7noMWJnjuHpYD1Sb4]
En el video se explica paso a paso como instalar y crear una aplicación Django.



## Elementos del proyecto 
Este proyecto consta de una sola aplicación [myapp] y un modelo de datos con 
dos conceptos: Project y Task, con relación de pertenencia: a un proyecto 
pertenecen 0, 1 ó mas tareas.

## Configurar el proyecto.
Se ha instalado un entorno virtual env, y para instalarlo ejecutamos desde 
la linea de comandos:
    PS C:\fuentes\PythonDjango> .\env\scripts\activate
    (env) PS C:\fuentes\PythonDjango> 

## Ejecutar la aplicación
Despues de activar el entorno.
Se pone en marcha con: 
-  python .\manage.py runserver 
-  acceder a la url: http://127.0.0.1:8000/