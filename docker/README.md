***Домашнее задание к лекции «Docker»***

**Задание 1**
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