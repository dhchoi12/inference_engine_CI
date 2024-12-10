# Inference Engine Flask 애플리케이션

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/inference", methods=["POST"])
def inference():
    data = request.json
    input_text = data.get("text", "No input provided")
    # 가상 모델 추론 결과
    prediction = f"[PREDICTION] Received input: {input_text}"
    return jsonify({"result": prediction})


@app.route("/", methods=["GET"])
def home():
    return "Inference Engine is Running!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
