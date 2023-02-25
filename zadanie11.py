from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = ""

    def handle_data(self, data):
        self.text += data

with open("C:/Users/Public/Zadanie11/11.html") as fp:
    parser = MyHTMLParser()
    parser.feed(fp.read())

# wyświetlenie wydobytego tekstu
print(parser.text)
