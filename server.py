from flask import Flask, jsonify, request
import json

app = Flask(__name__)

keywordSet = {"#ad, #sponsered", "advertisement"}

@app.route('/api/vocab', methods=['GET'])
def getVocab():
    print(keywordSet)
    res = dict.fromkeys(keywordSet, 0)
    return res

@app.route('/api/vocab', methods=['POST'])
def addVocab():
    keywordSet.add(request.get_json()["vocab"])
    print(keywordSet)
    res = dict.fromkeys(keywordSet,0)
    return res

@app.route('/api/prediction', methods=['POST'])
def predict():
    content = request.get_json()
    print(content)
    return


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)