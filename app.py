from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

@app.route("/receber-instrucao-gpt", methods=["POST"])
def receber_instrucao():
    data = request.json
    delivery_id = str(uuid.uuid4())
    response = {
        "status": "recebida",
        "delivery_id": delivery_id,
        "message": "Instrução recebida com sucesso pelo Webhook OPTMUS",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "modulo": data.get("modulo"),
        "origem": data.get("origem"),
        "processamento": "automatico",
        "versao_webhook": "1.0.0-render",
        "plataforma": "Render.com"
    }
    print("\n[Webhook Recebido]", response)
    return jsonify(response), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "Webhook GPT OPTMUS", "versao": "1.0.0-render"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
