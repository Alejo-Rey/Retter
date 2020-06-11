# Retter_human_resources

## How to run

create a file ```app.env```, put your info in this\
MYSQL_HOST=localhost\
MYSQL_PORT=port_mysql\
MYSQL_DATABASE=name_db\
MYSQL_USER=name_user\
MYSQL_PASSWORD=your_pwd\
MYSQL_ROOT_PASSWORD=root_pwd

run\
`sudo docker-compose run web django-admin startproject humanResources .`

modify the setting file, in this case 'humanResources/setting.py\
put this in the database info

```
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'USER': os.environ['MYSQL_USER'],
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
        'HOST': 'db',
        'PORT': os.environ['MYSQL_PORT'],
        'NAME': os.environ['MYSQL_DATABASE'],
    }
}
```

```sudo docker-compose run --rm web python manage.py makemigrations```