from flask import Flask, render_template, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# =====================
# HTML Routes
# =====================

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        """Render the main homepage."""
        return render_template("index.html")
    if request.method == "POST":
        user_input = request.form.get("")




# =====================
# Run the app
# =====================

if __name__ == "__main__":
    app.run(debug=True)
