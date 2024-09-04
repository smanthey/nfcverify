from flask import Flask, request

app = Flask(__name__)

# Main route
@app.route('/')
def home():
    return 'Hello, this is your Flask app on Heroku!'

# Route to handle NFC tag verification
@app.route('/nfc_verify/<tag_id>')
def nfc_verify(tag_id):
    # Simple logic to verify NFC tag
    if tag_id == "12345":  # Simulated tag ID
        return "NFC Tag Verified!"
    else:
        return "Verification Failed!"

if __name__ == '__main__':
    app.run(debug=True)
