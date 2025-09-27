from flask import Flask, render_template, jsonify, request
import ApiRequest as AR
import GLOBALS

link = GLOBALS.GPT_REQUEST_URL

# Initialize Flask app
app = Flask(__name__)

# =====================
# HTML Routes
# =====================

messages = []

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", messages=messages)

@app.route("/SubmitUserMessage", methods=["POST"])
def test():
    if request.method == "POST":
        data = request.form.get("data")
        if data:
            messages.append({"text": data, "sender": "user"})
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {GLOBALS.GPT_API_KEY}"
            }
            prompt = {
                "model": "gpt-4.1",
                "input": data
            }
            requestor = AR.ApiRequest()
            requestor.SendPostRequest(link, prompt, headers)
            dataToProcess = requestor.GetReturnData()
            messages.append({"text": dataToProcess, "sender": "system"})
        return render_template("index.html", messages=messages)




# =====================
# Run the app
# =====================

if __name__ == "__main__":
    app.run(debug=True)
