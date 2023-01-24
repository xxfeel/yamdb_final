## Проект: создание DevOps для YaMDb
[![yamdb_final](https://github.com/IvanFilippov74/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/IvanFilippov74/yamdb_final/actions/workflows/yamdb_workflow.yml)

### Описание:
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку. Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка».
### Технологии :
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)    ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
### Функционал:
-   Реализован REST API.
-   Используется аутентификация с помощью JWT-token.
-   Поддерживает методы GET, POST, PUT, PATCH, DELETE.

### Ресурсы
- Ресурс auth: аутентификация.
- Ресурс users: пользователи.
- Ресурс titles: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).
- Ресурс categories: категории (типы) произведений («Фильмы», «Книги», «Музыка»). Одно произведение может быть привязано только к одной категории.
- Ресурс genres: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.
- Ресурс reviews: отзывы на произведения. Отзыв привязан к определённому произведению.
- Ресурс comments: комментарии к отзывам. Комментарий привязан к определённому отзыву.
### Пользовательские роли и права доступа:
- Аноним — может просматривать описания произведений, читать отзывы и комментарии.
- Аутентифицированный пользователь (user) — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.
- Модератор (moderator) — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
- Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- Суперюзер Django обладает правами администратора, пользователя с правами admin.
### Как запустить проект:

1. Склонировать репозиторий в командной строке:
```
git clone https://github.com/IvanFilippov74/infra_sp2
```
Затем перейдите в корневую директорию проекта:
```
cd infra_sp2/
```
2. В корневой директории создайте файл .env, и заполните его:
```
SECRET_KEY=<секретный_ключ_проекта>
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<ваш_пароль>
DB_HOST=db
DB_PORT=5432
```
3. Если Docker не установлен, установите его используя официальную инструкцию:
```
https://docs.docker.com/engine/install/
```
4. Перейдите в директорию ```infra```:
```
cd infra/
```
Затем запустите docker-compose, используя команду*:
```
docker-compose up -d
```
5. Создайте миграции командой:
```
docker-compose exec web python manage.py migrate
```
6. Подгрузите статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
7. Заполните базу данных фикстурами:
```
docker-compose exec web python manage.py loaddata fixtures.json
```
8. Создайте супер пользователя (кроме пользователя admin):
```
docker-compose exec web python manage.py createsuperuser
```
9. Проект доступен по адресу ```http://localhost/```, для админ-панели используйте ```http://localhost/admin/```, документацию по api можно посмотреть здесь > ```http://localhost/redoc/```.
10. Остановить запущенные контейнеры можно командой ```docker-compose stop```, вновь запустить ```docker-compose start```, для остановки и удаления контейнеров используйте команду ```docker-compose down -v```.

*Важное примечание для ОС Linux используйте команду ```sudo```.
### Авторы
Филиппов Иван

<a href="https://github.com/IvanFilippov74"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"></a>