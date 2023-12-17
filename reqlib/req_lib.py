import requests

URL = "https://www.yahoo.co.jp"

# response = requests.get(URL)
# print(response.status_code)
# print(response.text)

# print(response.encoding)
# print(response.headers)

# for key, value in response.headers.items():
#     print(key, " ", value)

# print(response.cookies)

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
header = {"user-agent": user_agent}

# response = requests.get(URL, headers=header, timeout=3)
# print(response.status_code)
6
param = {"q": "anti-theft"}
response = requests.get("https://google.com/search", params=param)
print(response.status_code)
print(response.text)