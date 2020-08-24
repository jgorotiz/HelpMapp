# HelpMapp
Toda experiencia, buena o mala, sirve para aprender. En nuestro país, el terremoto del 16 de Abril marcó un antes y un después para las zonas afectadas; pero nos brindó la oportunidad de observar las falencias de los sistemas de ayuda inmediata y la necesidad de nuevos mecanismos que faciliten las acciones post-desastre; y a su vez aumenten la resiliencia de nuestras ciudades. Las fallas logísticas que sucedieron en el terremoto sirvieron al Gobierno central para reformar los manuales y protocolos de acción ante desastres, entre las reformas se anexaría la inclusión de los UPCs como centros de distribución de raciones alimenticias e insumos. En ese marco, presentamos “HelpMapp” una Aplicación que busca mejorar la logística de los centros de acopio post-desastre. Este mecanismo incluirá acceso a información fuera de línea, esquemas de actualización de datos mediante ondas de baja frecuencia y recomendaciones a usuarios sobre los centros de acopio más cercanos.

## Instalación y configuración
#### Autor: Piero Ulloa

Este proyecto se ha modernizado para funcionar en las versiones más recientes de Python y Django.
### Instalación de dependencias

Para instalar las dependencias, primero debes de crear un entorno virtual (venv), 
y luego en el entorno virtual ejecutar

```
pip install -r requierements.txt
```

Esto instalará las dependencias necesarias del proyecto en el venv, de modo que puedas ejecutarlo rápidamente.

Luego de descargar las dependencias, tienes que conectarte a una base de datos de PostgreSQL. 
Te recomiendo que leas daw/settings.py, y crees un usuario con los datos de conexión especificados en el archivo.

Para finalizar, debes de cargar la información inicial de la base de datos: el siguiente comando te ayudará con ello.

```
python manage.py loaddata sample_data/*.json
``` 

Luego de haber cargado la data de ejemplo, estás listo para correr el proyecto.


### Ejecución

Para ejecutar el proyecto de Django, simplemente debes de escribir en tu terminal: 

```
python manage.py runserver <port>
```

donde port es el puerto en el que deseas que la app escuche. NOTA: Esto no debe ser usado para correr un servidor de producción.
La aplicación debe ser montada en un servidor con interfaz WSGI, como nginx, o Apache (con mod_wsgi)

## Realización de Cambios

* Hacer pull del master para mantener tu repositorio local al día (cuando actualices desde el master, es posible que tengas que correr las migraciones, cuando haya cambios en la base de datos).
* Has todos los cambios necesarios para añadir una nueva característica o arreglar un bug en un nuevo branch.
* Prueba tus cambios localmente
* cambia el número de versión de la aplicación e indica los nuevos cambios realizados en el archivo CHANGELOG.md
* has commit de tus cambios y realiza el respectivo rebase con la rama master actualizada. (considerar esta [forma de hacer commit](https://tree.taiga.io/support/integrations/changing-elements-status-via-commit-message/))
* prueba DE NUEVO los cambios hechos localmente
* has push de tus cambios a un nuevo branch remoto con un nombre significativo
* crea un pull request y COMUNICA al equipo de desarrolladores para que revisen tus cambios hechos y que puedan agregar alguna observación
* espera a que tu pull request sea aprobado

## Referencias
--nada aún--
