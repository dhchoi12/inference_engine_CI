from flask import Flask, request, jsonify

app = Flask(__name__)

# Inference API (POST만 허용)
@app.route("/inference", methods=["POST"])
def inference():
    data = request.json
    input_text = data.get("text", "No input provided")
    prediction = f"[PREDICTION] Received input: {input_text}"
    return jsonify({"result": prediction})

# Home 엔드포인트 (GET 허용)
@app.route("/", methods=["GET"])
def home():
    return "Inference Engine is Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
