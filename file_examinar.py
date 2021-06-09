import bs4

file_name = input("File name: ")
with open(file_name) as input_file:
    parsed = bs4.BeautifulSoup(input_file.read(), "html.parser")

while (what_tag := input("What element do you want: ")) != "quit":
    print(f"The first {what_tag} is:\n{parsed.find(what_tag)}\n")
    print(f"The contents are:\n{''.join(str(tag) for tag in parsed.find(what_tag).contents)}\n")
    print(f"The attributes are:\n{parsed.find(what_tag).attrs}")
