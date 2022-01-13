from flask import Flask, render_template
app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/action_page.html")
def action():
    return render_template("action_page.html")


if __name__=="__main__":
    app.run()


