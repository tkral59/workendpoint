import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFICATION = "verifyToken_72cbd3b2-8fa9-41d4-a7e5-d234cf482fbe"
EP_URL = 'https://workendpoint.onrender.com/notifications'

@app.route('/notifications', methods=["GET", "POST"])
def handle_ebay_notification():
    if request.method == "GET":
        challenge = request.args.get("challenge_code")
        if not challenge:
            return jsonify({"error": "Missing challenge_code"}), 400

        to_hash = challenge + VERIFICATION + EP_URL
        hash_obj = hashlib.sha256(to_hash.encode('utf-8'))
        challenge_response = hash_obj.hexdigest()

        return jsonify({"challengeResponse": challenge_response}), 200
    elif request.method == "POST":
        data = request.get_json()
        print("Received notifications:", data)
        return jsonify({'status':'received'}), 200

@app.route('/')
def index():
    return "eBay Endpoint is running", 200

if __name__ == "__main__":
    app.run()


