from flask import Flask, render_template, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# =====================
# HTML Routes
# =====================

messages = []

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/SubmitUserMessage", methods=["POST"])
def test():
    if request.method == "POST":
        data = request.form.get("data")
        if data:
            messages.append(data)
        return render_template("index.html", messages=messages)




# =====================
# Run the app
# =====================

if __name__ == "__main__":
    app.run(debug=True)
