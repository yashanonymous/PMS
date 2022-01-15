from flask import Flask, render_template
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)


@app.route("//")
def home():
    return render_template("index.html")


@app.route("/action_page.html")
def action():
    return render_template("action_page.html")


if __name__ == "__main__":
    app.run(debug=True)
