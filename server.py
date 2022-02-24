from flask import Flask, jsonify, request
import json

app = Flask(__name__)

keywordSet = {"#ad", "#sponsered", "advertisement"}

@app.route('/api/vocab', methods=['GET'])
def getVocab():
    res = dict.fromkeys(keywordSet, 0)
    return res

@app.route('/api/vocab', methods=['POST'])
def addVocab():
    keywordList = request.get_json()["vocab"]
    for x in keywordList:
        keywordSet.add(x)
    res = dict.fromkeys(keywordSet,0)
    return res

@app.route('/api/prediction', methods=['POST'])
def predict():
    postText = request.get_json()["post_text"]
    postWordsSet = set(postText.split(" "))
    dict = {"prediction": "non-sponsored"}
    if keywordSet.intersection(postWordsSet):
        dict["prediction"] = "sponsored"
    return dict


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)