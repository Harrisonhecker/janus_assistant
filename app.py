from flask import Flask, render_template, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# =====================
# HTML Routes
# =====================

@app.route("/")
def home():
    """Render the main homepage."""
    return render_template("index.html")

# =====================
# Run the app
# =====================

if __name__ == "__main__":
    app.run(debug=True)
