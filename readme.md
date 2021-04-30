### Установка и запуск проекта
***
```
pip install -r requirements_nix.txt
```
или же для windows извращенцев
```
pip install -r requirements_win.txt
```
Далее создать в корне проекта файл `.env` и указать данные для подключения к БД⋅⋅
Атеншен, `postrgres`.
```
NAME= DBNAME
USER= DBUSERNAME
PASSWORD= DBPASSWORD
```
Далее стандарный локальный запуск django проекта.Как это сделать вы и так в курсе :)
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Документация к api в swagger
```
http://127.0.0.1:8000/swagger/
```
Авторизация по JWT 
```
curl --location --request POST 'http://127.0.0.1:8000/auth/jwt/create/' \
--form 'username="username"' \
--form 'password="password"'
```
Для ednpoint, с permission  `IsAdminUser` в хедер запросов добавить полученный токен с приставкой `Bearer`
```
curl --location --request POST 'http://127.0.0.1:8000/api/v1/user_answer_create' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE5NzMzMzg2LCJqdGkiOiI2NjQ1ZDA0OWJhMTQ0NDA2YjdhMTkzYTRiZDFiNTVhZCIsInVzZXJfaWQiOjF9.NrwDv4zn1n4441UUa_ekyX6q4WNiikKurs15iPX-mEI' \
--form 'user="1"' \
--form 'survey="6"' \
--form 'question="2"' \
--form 'answer_option="4"' \
--form 'user_answer="Apple"'
```
В целом все требования из ТЗ удовлетворены, хотя "полировать" любой проект можно до бесконечности. Некоторые этапы валидаций, например проверка на количество ответов для вопроса с single answer я оставил на совести абстрактного фронтэндера.
На текущий момент это хороший MVP :)
