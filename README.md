# Tercera-pre-entrega-DelCastilloGomezAdolfo

Este es la ultima entrega del curso Python en CoderHouse!

> Autor:
- Alumno: Adolfo Del Castillo Gomez

## Configuracion previa instalacion de software.

- Python version: Python 3.11.6
- sqlite version: SQLite 3.0
- django version: django 4.2.7


## Crear la DB y crear arquitectura de DB.

En la consolo ejecutaremos los siguientes comandos para incializar la DB y crear la estructura:

En la carpeta /tercer_proyecto/ buscamos el archivo manage.py

    $ python3 manage.py makemigrations
    $ python3 manage.py migrations
    >>>

Una vez ejecutado los comandos se creara el archivo db.sqlite3 donde tendremos nuestra DB.

## Inicializar servidor web.

En la consola de tu equipo ejecuta el siguiente comando:

    $ python3 manage.py runserver
    >>>

Una vez ejecutado entraras a la siguiente URL desde algun browser en tu equipo donde esta corriento tu servicio web:

- http://127.0.0.1:8000/

## Sitio Web.

Una vez en el sitio podremos ver que en la raiz tenemos dos apartados:

- admin/
- app/
- accounts/

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/blog_adolfo_del_castillo/imag/Image1.png)

Para comenzar a navegar nos iremos a la seccion del CV:

- http://127.0.0.1:8000/app/about_me/

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/blog_adolfo_del_castillo/imag/Image2.png)

Si queremos tratar de ir a la seccion de Usuarios, Publicar y no hemos logeado nos mostrara la siguiente pantalla:

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/blog_adolfo_del_castillo/imag/Image3.png)

Ya que es necesario logearse previamente para poder acceder a estas secciones.

Si entramos a la seccion de Publicaciones veremos los datos de las publicaciones solo el nombre, el titulo y la fecha:

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/blog_adolfo_del_castillo/imag/Image4.png)

Si nosotros seleccionamos detalles no nos permitira acceder por temas de permisos si es que aun no estamos logeados.

En el menu de Logeo nos mostrara la opcion de colocar nombre y contrasenia o crear un nuevo usuario:

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/blog_adolfo_del_castillo/imag/Image5.png)

Si nos logeamos correctamente nos permitira a aceder a los detalles de las publicaciones, si nos logeamos y nuestro usuario tiene rol de super usuario podremos entrar a ver la lista de los usuarios creados.

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/blog_adolfo_del_castillo/imag/Image6.png)

Si el usuario logeado no tiene rol de super usuario se mostrara el siguiente mensaje en la seccion de usuario.

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](/blog_adolfo_del_castillo/imag/Image7.png)
