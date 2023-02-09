from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # parse XML file
    with open("C:/Users/steev/PycharmProjects/pythonProject/sample.xml") as f:
        soup = BeautifulSoup(f, "xml")

    # extract data from XML
    data = []
    for item in soup.find_all("item"):
        title = item.title.text
        description = item.description.text
        link = item.link.text
        data.append({"title": title, "description": description, "link": link})

    # render template with extracted data
    return render_template("demo.html", data=data)


if __name__ == "__main__":
    app.run()
