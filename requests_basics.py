import requests
import bs4

response = requests.get("https://www.google.com/search?q=cat")
# print(response.status_code)  # Gets status code (for example: 200, 400)
# print(response.text)         # Gets the content of the response in Unicode
# print(response.content)      # Gets the content of the response in bytes
# print(response.json())       # Gets the content of the response as a dictionary (JSON)
# print(response.headers)      # Gets the headers
# print(response.cookies)      # Gets the cookies
# print(response.url)          # Gets the url of request

"""
r.text is the content of the response in Unicode, and r.content is
the content of the response in bytes.
"""

# if response.status_code == 200:  # Status code for success
#     print(response.text, type(response.text))
#     # Prints out as string, because print convert the thing it is printing to
#     # a string
#     print(response.content, type(response.content))

parsed = bs4.BeautifulSoup(response.text, "html.parser")
print(parsed.find_all("a"))
print([link.text for link in parsed.find_all("a")])
