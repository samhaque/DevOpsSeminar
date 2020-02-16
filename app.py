import os

from flask import Flask, request, jsonify

VERIFICATION_SECRET = os.getenv("VERIFICATION_TOKEN")

app = Flask(__name__)


@app.route('/', methods=["POST"])
def gnome_channel():
    print(request.form)
    if request.form['token'] == VERIFICATION_SECRET:
        return jsonify({
            "response_type": "in_channel",
            "attachments": [
                {
                    "title": "You've been Gnomed",
                    "image_url": "https://thumbs.gfycat.com/SaneDisgustingAtlanticridleyturtle-max-1mb.gif"
                }
            ]
        })
    return jsonify({
        "response_type": "ephemeral",
        "text": "Sorry, that didn't work. Please try again."
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
