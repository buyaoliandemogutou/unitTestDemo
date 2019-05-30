import requests

response=requests.get('http://www.baidu.com')

print(response.url)
print(response.headers)
print(response.cookies)
print(response.text)
print(response.content)