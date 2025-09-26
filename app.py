from flask import Flask, render_template, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# =====================
# HTML Routes
# =====================

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        data = request.form.get("data")
        print(f"Received data: {data}")
        return render_template("test.html", data=data)

    return render_template("test.html")




# =====================
# Run the app
# =====================

if __name__ == "__main__":
    app.run(debug=True)
