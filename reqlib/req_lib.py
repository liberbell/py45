import requests

URL = "https://www.yahoo.co.jp"

response = requests.get(URL)
# print(response.status_code)
# print(response.text)

# print(response.encoding)
print(response.headers)

for key, value in response.headers.items():
    print(key, " ", value)