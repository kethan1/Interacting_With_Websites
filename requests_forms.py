import requests

# The dictionary keys correspond to the name attributes of the HTML input elements.
form_values = {"username": "cat", "password": "cat123"}
response1 = requests.post("http://www.httpbin.org/post", data=form_values)
response2 = requests.post("http://www.httpbin.org/post", json=form_values)
with open("file.html", "rb") as to_send:
    response3 = requests.post("http://www.httpbin.org/post", files={'upload_file': to_send})

print(response1.json())
print(response2.json())
# print(response3.json())

"""
Some websites block HTTP requests that come from bots (or at least try to)

To get around this, pass some headers to either requests.get() or requests.post():
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
"""
