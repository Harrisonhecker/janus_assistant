from flask import Flask, render_template, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# =====================
# HTML Routes
# =====================

messages = {}

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", messages=messages)

@app.route("/SubmitUserMessage", methods=["POST"])
def test():
    if request.method == "POST":
        data = request.form.get("data")
        if data:
            messages[data] = "User"

            # TODO: research how to call ollama API, call it here
            
            ollamaResponse = ""
            messages[ollamaResponse] = "System"
        return render_template("index.html", messages=messages)




# =====================
# Run the app
# =====================

if __name__ == "__main__":
    app.run(debug=True)
