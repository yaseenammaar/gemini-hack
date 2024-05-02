from flask import Flask, render_template, request, jsonify
from flights import search_flights
from hotels import search_hotels
from group_booking import calculate_group_discount

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    search_type = request.form.get("search_type")
    origin = request.form.get("origin")
    destination = request.form.get("destination")
    date = request.form.get("date")
    group_id = request.form.get("group_id")

    if search_type == "flights":
        results = search_flights(origin, destination, date, group_id)
    elif search_type == "hotels":
        results = search_hotels(destination, date, group_id)
    else:
        results = []

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
