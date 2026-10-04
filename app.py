from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def home():

    with open("data/certificates.json", "r", encoding="utf-8") as file:
        certificates = json.load(file)

    return render_template(
        "index.html",
        certificates=certificates
    )


if __name__ == "__main__":
    app.run(debug=True)