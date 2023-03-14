from requests import get, post, delete

print(get('http://localhost:5001/api/v2/news').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:5001/api/news/1').json())