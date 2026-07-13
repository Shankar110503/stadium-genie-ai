from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key=AQ.Ab8RN6KyV74XJGn2htPP-fj1-4ta5l8jAxcRSp_lWZk7idp9tA)

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

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = model.generate_content(
        SYSTEM_PROMPT + "\nUser: " + user_message
    )

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)
