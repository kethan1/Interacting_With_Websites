import bs4

while True:
    try:
        with open(input("File name: ")) as input_file:
            parsed = bs4.BeautifulSoup(input_file.read(), "html.parser")
        break
    except FileNotFoundError:
        print("File Not Found")

while (what_tag := input("What element do you want: ")) != "quit":
    for element_found in parsed.select(what_tag):
        print(f"- {element_found}, \n   contents: {''.join(str(tag) for tag in element_found.contents)}, \n   attributes: {element_found.attrs}")
