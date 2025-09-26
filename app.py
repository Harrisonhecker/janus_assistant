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
            # 1. build dictionary of request data (make sure stream parameter set to false)
            # 2. establish link that we want to send request to (http://localhost:11434/api/generate)
            # 3. Use ApiRequest class to send the request and get the response
            # 4. Set the response to ollamaResponse variable

            ollamaResponse = ""
            messages[ollamaResponse] = "System"
        return render_template("index.html", messages=messages)




# =====================
# Run the app
# =====================

if __name__ == "__main__":
    app.run(debug=True)
