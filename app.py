from flask import Flask, request

app = Flask(__name__)

# List of valid NFC tag UIDs for verification
valid_tag_uids = {
    "04:63:1A:F5": "Verified Tag"  # Replace this with your NFC tag UID
}

@app.route('/nfc_verify')
def nfc_verify():
    uid = request.args.get('uid')  # Get the UID from the URL query parameter
    
    if uid in valid_tag_uids:
        return f"NFC Tag Verified for {valid_tag_uids[uid]}"
    else:
        return "Verification Failed!"

if __name__ == '__main__':
    app.run(debug=True)
