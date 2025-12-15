from flask import Flask, request, session, jsonify, make_response

app = Flask(__name__)
app.json.compact = False

# Note: Flask app secret keys should not be publicly accessible for deployed applications
# You can store secret keys in environment variables and use packages like dotenv
app.secret_key = b'?w\x85Z\x08Q\xbdO\xb8\xa9\xb65Kj\xa9_'

# Build Routes

if __name__ == '__main__':
    app.run(port=5555)
    