from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit

url_url = "https://lpgenerator.ru:8081/blog/2011/04/25/url-adresa-i-celevye-stranicy/"

url = urlparse(url_url)

tup_url = tuple(url)

print("Протокол: ",url.scheme)
print("Домен: ",url.hostname)
print("Номер порта: ",url.port)
print("Путь: ",url.path)
print("Параметры: ",url.params)
print("Строка запроса: ",url.query)
print("Якорь: ",url.fragment)

print(urlunparse(tup_url))

ftp = urlparse("ftp://user:123456@mysite.ru")

print("Имя пользователя: ",ftp.username,
      "\nПароль: ",ftp.password)

new_url = urlsplit(url_url)

print(urlunsplit(new_url) )
