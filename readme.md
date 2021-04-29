### Установка и запуск проекта
***
```
pip install -r requirements_nix.txt
```
или же для windows извращенцев
```
pip install -r requirements_win.txt
```
Далее создать в корне проекта файл `.env` и указать данные для подключения к БД  Атеншен, `postrgres`.
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

В целом все требования из ТЗ удовлетворены, хотя "полировать" любой проект можно до бесконечности. Некоторые этапы валидаций, например проверка на количество ответов для вопроса с single answer я оставил на совести абстрактного фронтэндера.
На текущий момент это хороший MVP :)
