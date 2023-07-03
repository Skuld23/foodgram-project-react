[![.github/workflows/foodgram-workflow.yml](https://github.com/Skuld23/foodgram-project-react/actions/workflows/foodgram-workflow.yml/badge.svg)](https://github.com/Skuld23/foodgram-project-react/actions/workflows/foodgram-workflow.yml)
##  Описание
Foodgram - продуктовый помощник с базой кулинарных рецептов. Позволяет публиковать рецепты, сохранять избранные, а также формировать список покупок для выбранных рецептов. Можно подписываться на любимых авторов.

### Технологии:
Python, Django, Django Rest Framework, Docker, Gunicorn, NGINX, PostgreSQL, Yandex Cloud, Continuous Integration, Continuous Deployment
### Инструкция по развёртыванию:
1. Загрузите проект.
```
git clone git@github.com:Skuld23/foodgram-project-react.git
```
2. Подключиться к вашему серверу.
```
ssh <server user>@<server IP>
```
3. Установите Докер на свой сервер.
```
sudo apt install docker.io
```
4. Получить разрешения для docker-compose.
```
sudo chmod +x /usr/local/bin/docker-compose
```
5. Создайте env-файл.
```
nano.env
```
6. Заполните env-файл.
```

SECRET_KEY = указываем секретный ключ Django из файла settings.py
DB_ENGINE = указываем тип БД default='django.db.backends.postgresql'
DB_NAME = имя базы данных
POSTGRES_USER = логин для подключения к базе данных
POSTGRES_PASSWORD = пароль для подключения к БД (установите свой)
DB_HOST = название сервиса (контейнера)
DB_PORT = порт для подключения к БД
```
8. Скопируйте файлы из 'infra/' с ПК на ваш сервер.
```
scp infra/* <server user>@<server IP>:/home/<server user>/foodgram/
```
9. Запустите docker-compose.
```
sudo docker-compose up -d --build
```
10. Запустите миграции.
```
sudo docker compose exec -T backend python manage.py makemigrations
sudo docker compose exec -T backend python manage.py migrate
```
11. Запустите сбор статики.
```
sudo docker compose exec backend python manage.py collectstatic --noinput
```
12. Создайте супер пользователя.
```
sudo docker compose exec backend python manage.py createsuperuser
```
13. Загрузите подготовленный список ингредиентов для работы с проектом
```
sudo docker compose exec backend python manage.py load_tags
sudo docker compose exec backend python manage.py load_inrgs
```

### Настроен Workflow, который состоит из четырех шагов:
- Проверка кода на соответствие PEP8
- Сборка и публикация образа бекенда на DockerHub.
- Автоматический деплой на удаленный сервер.
- Отправка уведомления в телеграм-чат.

### Actions secrets
- `SECRET_KEY` = указываем секретный ключ Django из файла settings.py
- `DB_ENGINE` = указываем тип БД `default='django.db.backends.postgresql'`
- `DB_NAME = postgres` # имя базы данных
- `POSTGRES_USER = postgres` # логин для подключения к базе данных
- `POSTGRES_PASSWORD = postgres` # пароль для подключения к БД
- `DB_HOST = db` # название сервиса (контейнера)
- `DB_PORT = 5432` # порт для подключения к БД
- `DOCKER_PASSWORD` = пароль от DockerHub
- `DOCKER_USERNAME` = логин DockerHub
- `HOST` = адрес вашего удаленного сервера
- `SSH_KEY` = Скопируйте приватный ключ с компьютера командой 
- `TELEGRAM_TO` = ваш id в телеграме
- `TELEGRAM_TOKEN` = токен моего телеграм бота 
- `USER` = логин на вашем удаленном сервере
- `PASSPHRASE` = пароль от сервера

<h2>Проект доступен по адресу 
158.160.108.186

  ## Пользователи 

- супер юзер - qqq@qqq.qq  пароль qqq 
- www@www.ww пароль qwertqwe
- aaa@aaa.aa пароль qwertqwe
