from flask import Flask, request, jsonify
import random

app = Flask(__name__)

roasts = [
    "Your code is so messy, even Git refused to commit it.",
    "You have more TODOs than working functions.",
    "You write code like it's a secret — even you can't read it.",
    "Stack Overflow called. They want their questions back.",
    "Your last PR was labeled a 'crime scene'.",
    "You use print statements like duct tape.",
    "Your code compiles, but at what cost?",
    "If bugs were art, you'd be Picasso."
]

@app.route('/roast')
def roast():
    name = request.args.get('name')
    burn = random.choice(roasts)

    if name:
        burn = f"{name}, {burn}"
    return jsonify(roast=burn)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
