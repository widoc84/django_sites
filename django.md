# Создание сущностей
## Модуль django-admin
1. django-admin startproject %имя проекта% - создание проекта

## Модуль manage
### Управление миграциями
1. python manage.py makemigrations - создание миграций
2. python manage.py sqlmigrate %база% %id миграции% - проверка запроса
3. python manage.py migrate - выполнение миграций

### Прочие команды
1. python manage.py runserver - run server
2. python manage.py shell - run shell
3. python manage.py startapp %name module% - create new app

