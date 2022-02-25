from flask import Flask, jsonify, request
import json
import os

baseKeywords = {"vocab": ["#ad", "#sponsored", "advertisement"]}

dbFilePath = "keywords.json"

if not os.path.exists(dbFilePath):
    fd = open(dbFilePath, 'w')
    json_string = json.dumps(baseKeywords)
    json.dump(json_string, fd)
    fd.close()

fd = open(dbFilePath, "r")
json_string = json.load(fd)
dic = json.loads(json_string)
keywordSet = set(dic["vocab"])
fd.close()

app = Flask(__name__)

@app.route('/api/vocab', methods=['GET'])
def getVocab():
    res = {}
    res["vocab"] = list(keywordSet)
    return res

@app.route('/api/vocab', methods=['POST'])
def addVocab():
    newKeywordList = request.get_json()["vocab"]
    if len(newKeywordList) > 0:
        for x in newKeywordList:
            keywordSet.add(x)
        fd = open(dbFilePath, "w")
        dic = {"vocab": list(keywordSet)}
        json_string = json.dumps(dic)
        json.dump(json_string, fd)
        fd.close()
    res = {}
    res["vocab"] = list(keywordSet)
    return res

@app.route('/api/prediction', methods=['POST'])
def predict():
    postText = request.get_json()["post_text"].lower()
    res = {"prediction": "non-sponsored"}
    for x in keywordSet:
        if x.lower() in postText:
            res["prediction"] = "sponsored"
            break
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)