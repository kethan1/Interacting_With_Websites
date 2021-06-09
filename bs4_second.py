import bs4

with open("file.html") as input_file:
    html = input_file.read()

parsed = bs4.BeautifulSoup(html, "html.parser")

print(parsed.find("p", {"id": "testid"}))
print(parsed.find("p", {"class": "test_class"}))
print(parsed.find("p", {"id": "testid2", "class": "test_class"}))
print(parsed.find("p", {"class": "test_class"}, string="Toss"))
