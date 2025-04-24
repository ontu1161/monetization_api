from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Monetization API is running!"

@app.route('/check', methods=['POST'])
def check_monetization():
    data = request.json
    channel_id = data.get('channel_id')

    import requests

# API Key দরকার হবে
API_KEY = "YOUR_YOUTUBE_API_KEY"
URL = f"https://www.googleapis.com/youtube/v3/channels?part=monetizationDetails&id={channel_id}&key={API_KEY}"

res = requests.get(URL).json()
# তারপর রেসপন্স থেকে তোমার প্রয়োজনীয় ডেটা বের করে দেখাতে পারো
    # আমরা এখন শুধু ডেমো রেসপন্স দিচ্ছি।
    response = {
        "channel_id": channel_id,
        "eligible": True,
        "message": "Channel is eligible for monetization."
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)