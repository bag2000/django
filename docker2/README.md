***Домашнее задание к лекции «Docker»***

**Задание 2**
smart_home - мое приложение
```
root@srv1:/home/adm2/netology# ls
Dockerfile  smart_home
```
Создаем Dockerfile
```
root@srv1:/home/adm2/netology# cat Dockerfile
FROM python:3.8
WORKDIR /smart_home
COPY ./smart_home /smart_home
RUN pip install -r /smart_home/requirements.txt
RUN python manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
```
Создаем образ с названием smart_home:1.0
```
root@srv1:/home/adm2/netology# docker build . --tag smart_home:1.0
```
Запускаем контейнер используя образ smart_home:1.0 и открываем порт 8000
```
root@srv1:/home/adm2/netology# docker run -p 8000:8000 smart_home:1.0
```
Выполняем запросы. Примеры в файле smart_home/requests.http