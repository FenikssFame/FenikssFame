from urllib.parse import urlparse, urlunparse

url_url = "http://www.user.by:50/test.php;st?var=10#metka"
port_num = input("Введите номер порта:")

url = urlparse(url_url)

tup_url = tuple(url)



print("Протокол: ",url.scheme)
print("Домен: ",url.hostname)
print("Номер порта: ",url.port)
print("Путь: ",url.path)
print("Параметры: ",url.params)
print("Строка запроса: ",url.query)
print("Якорь: ",url.fragment)

url_collect = urlunparse(tup_url)

print(url_collect)
