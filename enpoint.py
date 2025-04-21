from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFICATION = "verifyToken_72cbd3b2-8fa9-41d4-a7e5-d234cf482fbe"

@app.route('/api/ebay/deletion', methods=["POST"])
def handle_ebay_notification():
    data = request.json

    if "challengeCode" in data:
        if data.get("verificationToken") == VERIFICATION:
            return jsonify({"challengeResponse": data["challengeCode"]})
        else:
            return jsonify({"error": "Invalid token"}), 401
        
    ebay_user_id = data.get("userId")
    print(f"eBay account deletion for user: {ebay_user_id}")

    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run()