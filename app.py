from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index(name=None):
    return render_template("index.html", name=name)


@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("search.html")


@app.route("/get_all_relation", methods=["GET", "POST"])
def get_all_relation():
    return render_template("all_relation.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
