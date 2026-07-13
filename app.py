from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

app = Flask(__name__)

# Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

SYSTEM_PROMPT = """
You are StadiumGenie AI.

Help football fans and stadium staff.

Answer in the user's preferred language.

Provide navigation, safety guidance, crowd management advice,
transport information, accessibility support,
and emergency instructions.

Always give short, accurate, and helpful responses.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_message = data.get("message", "")

    prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_message}"

    response = model.generate_content(prompt)

    return jsonify({
        "reply": response.text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
