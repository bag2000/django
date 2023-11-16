# Домашнее задание к лекции «Docker»

## Задание 1

По аналогии с практикой из лекции создайте свой docker image с http сервером nginx. Замените страницу приветсвия Nginx на своё (измените текст приветствия на той же странице).

<details>
<summary>Подсказки:</summary>
В официальном образе nginx стандартный путь к статичным файлам `/usr/share/nginx/html`.  
</details>

На проверку присылается GitHub-репозиторий с Dockerfile и статичными файлами для него.

> Для пользовательского html можно использовать пример в [каталоге](html/) с ДЗ.

**Ответ**
```
root@srv1:/home/adm2/netology2# cat index.html
<html>
<head>
Hey, Netology
</head>
<body>
<h1>I’m student!</h1>
</body>
</html>

root@srv1:/home/adm2/netology2# cat Dockerfile
FROM nginx
COPY ./index.html /usr/share/nginx/html/index.html
CMD ["nginx", "-g", "daemon off;"]

root@srv1:/home/adm2/netology2# docker build . --tag my-nginx:1.0
root@srv1:/home/adm2/netology2# docker run -p 9090:80 my-nginx:1.0
http://192.168.12.17:9090/
```