import requests

response=requests.get('http://www.baidu.com')
print('status_code:',response.status_code)
print(response.url)
print(response.headers)
print(response.cookies)
print(response.text)
print(response.content)

payload={'key1':'2','key2':'value2'}
r=requests.get('http://httpbin.org/get',params=payload)
print(r.url)
print(r.content)
print(r.headers)
print('cookies',r.cookies)
print('json:',r.json())

payload={'key1':'value1','key2':'value2'}
r1=requests.post('http://httpbin.org/post',data=payload)
print(r1.json())
print(r1.url)
print(r1.text)