from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Monetization API is running!"

@app.route('/check', methods=['POST'])
def check_monetization():
    data = request.json
    channel_id = data.get('channel_id')

    # এখানে তুমি ইউটিউব API দিয়ে চ্যানেল চেক করতে পারো।
    # আমরা এখন শুধু ডেমো রেসপন্স দিচ্ছি।
    response = {
        "channel_id": channel_id,
        "eligible": True,
        "message": "Channel is eligible for monetization."
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)