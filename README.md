# curso

1. activar entorno virtual:
   1. LINUX : source rutaRelativaAVenv/bin/activate
   2. Window: rutaRelativaAVenv/Scripts/activate
2. ejecutar => pip install -r requirements.txt
3. entrar en PgAdmin4 y crear una Bases de datos nueva llamada 'db_user_project'
4. ejecutar => python manage.py migrate
5. crear primer usuario ejecutando => python manage.py createsuperuser
