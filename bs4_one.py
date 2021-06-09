import bs4
import webbrowser

with open("file.html") as input_file:
    html = input_file.read()

parsed = bs4.BeautifulSoup(html, "html.parser")

print(f"Parsed HTML: {parsed}")
print(f"First a tag: {parsed.find('a')}")
print(f"First button tag: {parsed.button}")
print(f"Contents of the first div: {parsed.div.contents}")
print(f"Contents of the first div's first div: {parsed.div.div.contents}")
print(f"href's of all the a tags: {[tag['href'] for tag in parsed.find_all('a')]}")
print("\nAll the children of the first div: ")
for child in parsed.div:
    print(child)
print("\nAll the parents of the element p with id hi: ")
for parent in parsed.find("p", {"id": "testid"}).parents:
    print(f"\n{parent}")

# Program to print open all the link on a page:
# for link in [tag["href"] for tag in parsed.find_all("a")]:
#     webbrowser.open(link)
