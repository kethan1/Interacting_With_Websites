import requests
import bs4

# url = input("Enter the website's url: ")
url = "https://blogger-101.herokuapp.com/login"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})

parsed = bs4.BeautifulSoup(response.text, "html.parser")

input_elements = [
    [
        [input_to_send["name"], input_to_send["type"]]
        for input_to_send in form.select("input")
    ]
    for form in parsed.select("form[method=POST]")
]


to_send = {}
for index, input_elements_per_form in enumerate(input_elements):
    print(f"Form #{index}")
    if parsed.select("form[method=POST]")[0].get('action') is None:
        to_post_url = url
    else:
        to_post_url = parsed.select("form[method=POST]")[0].get('action')
    data = {}
    for index, input_element in enumerate(input_elements_per_form):
        data[input_element[0]] = input(f"Input Element #{index}. Name: {input_element[0]}, Type: {input_element[1]}: ")
    to_send[to_post_url] = data

print(to_send)
for key, value in to_send.items():
    print(requests.post(key, data=value).text)
