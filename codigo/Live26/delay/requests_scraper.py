import requests


for delay in [1, 2, 3, 4, 5]:
    url = f"http://httpbin.org/delay/{delay}"
    requests.get(url)
    print(url)
