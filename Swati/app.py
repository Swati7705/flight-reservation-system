from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulate a database
flights = [
    {"id": 1, "destination": "New York", "price": 500},
    {"id": 2, "destination": "London", "price": 700},
    {"id": 3, "destination": "Paris", "price": 600},
    {"id": 4, "destination": "India", "price": 800}
]

reservations = []

@app.route("/")
def home():
    return render_template("index.html", flights=flights)

@app.route("/reserve/<int:flight_id>", methods=["GET", "POST"])
def reserve(flight_id):
    flight = next((f for f in flights if f["id"] == flight_id), None)
    if not flight:
        return "Flight not found", 404

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        reservations.append({"flight_id": flight_id, "name": name, "email": email})
        return redirect(url_for("success", flight_id=flight_id, name=name))

    return render_template("reserve.html", flight=flight)

@app.route("/success")
def success():
    name = request.args.get("name")
    flight_id = int(request.args.get("flight_id"))
    flight = next((f for f in flights if f["id"] == flight_id), None)
    return render_template("success.html", name=name, flight=flight)

if __name__ == "__main__":
    app.run(debug=True)
