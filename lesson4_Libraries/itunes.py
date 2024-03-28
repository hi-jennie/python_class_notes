import requests
import sys

if len(sys.argv) != 2:
    sys.exit

response = requests.get(
    "http://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
# print(json.dumps(response.json(), indent=2))
# json是js对象表示法


o = response.json()  # o是一个dict
for result in o["results"]:  # o这个dict里面名为“result”的key所对应的value
    print(
        result["trackName"]
    )  # “results”所对应的value又是一个dict，print result中名为“trackName"所对应的value。
