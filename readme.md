# infinity tech Test Backend

## Instructivos para correr la aplicación:

- instalar los modulos django djangorestframework y psycopg2 utilizando pip
- Correr `python manage.py` en la CLI cuando se encuentre ubicado dentro del folder del proyecto.
- para la base de datos no es necesario generarla , se creo una instancia de PostgresSQL utilizando
  Amazon RDS para evitar problemas de migraciones entre otras cosas

## Breve explicación de lo que hace el aplicativo:

- La aplicación simula un **Admin Panel** o un **Dashboard** en el cuál podrá navegar a través del sidebar.

## Básica estructuración de folders.

| Folder   | Explicacion                                                                   |
| -------- | ----------------------------------------------------------------------------- |
| Api      | Aquí va todo lo relacionado a la de negocios y endpoints de la API.           |
| Base     | Aquí va todo lo relacionado a los modelos que se usaron para la base de datos |
| Material | aquí va la configuración de django                                            |
