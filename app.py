from flask import Flask, request

app = Flask(__name__)

# List of valid NFC tag UIDs
valid_tag_uids = {
    "04:63:1A:F5": "Tag 1",
    "04:63:XX:YY": "Tag 2"  # Add more tags here
}

@app.route('/nfc_verify')
def nfc_verify():
    uid = request.args.get('uid')  # Get UID from the query string
    
    if uid in valid_tag_uids:
        return f"NFC Tag Verified for {valid_tag_uids[uid]}"
    else:
        return "Verification Failed!"

if __name__ == '__main__':
    app.run(debug=True)
