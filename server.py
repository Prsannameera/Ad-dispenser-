
from flask import Flask, jsonify

app = Flask(__name__)

ads = ["Buy Now!", "Flash Sale!", "Visit Our Store!", "50% Off!"]

@app.route('/ads', methods=['GET'])
def get_ads():
    import random
    return jsonify({"ad": random.choice(ads)})

if __name__ == '__main__':
    app.run(debug=True)
