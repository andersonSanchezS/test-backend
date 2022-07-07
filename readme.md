# infinity tech Test Backend

## Instructivos para correr la aplicación:

- instalar los modulos django djangorestframework y psycopg2, django-cors-headers utilizando pip
- Correr `python manage.py` en la CLI cuando se encuentre ubicado dentro del folder del proyecto.
- para la base de datos no es necesario generarla , se creo una instancia de PostgresSQL utilizando
  Amazon RDS para evitar problemas de migraciones entre otras cosas
2
## Pruebas de los endpoints
- en el archivo request.example.http se encuentran las pruebas de los endpoints las urls y los que se tiene que
enviar en el body de la petición, para poder ejecutar los endPoints en de este archivo es necesario instalar 
una extension de visual studio code llamada REST Client.
link : https://marketplace.visualstudio.com/items?itemName=humao.rest-client
## Básica estructuración de folders.

| Folder     | Explicacion                                                                   |
| --------   | ----------------------------------------------------------------------------- |
| Api        | Aquí va todo lo relacionado a la de negocios y endpoints de la API.           |
| Base       | Aquí va todo lo relacionado a los modelos que se usaron para la base de datos |
| LeagueCrud | aquí va la configuración de django                                            |
