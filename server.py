from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", cupcakes = get_cupcakes("cupcakes.csv"))

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html")

@app.route("/cupcake_individual/<name>")
def individual_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)
    return render_template("individual-cupcake.html", cupcake=cupcake)

@app.route("/order")
def order():
    return render_template("order.html")


@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."


if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, host="localhost", port=5000)