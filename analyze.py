import json
import collections
import flask

app = flask.Flask(__name__)
@app.route("/analyze")
def index(request):

    # some JSON:
    x =  '{"text":"hello 2 times  "}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    # print(y["text"])
    text = y["text"]

    charFreqs = { }

    spacesNum = 0

    wordCount = text.split();
    wordsNum = len(wordCount)

    for ch in text:
        if ch == ' ':
            spacesNum = spacesNum + 1
            continue
        if ch >= '0' and ch <= '9':
            continue

        if ch in charFreqs.keys():
            charFreqs[ch] = charFreqs[ch] + 1;
        else:
            charFreqs[ch] = 1

    od = collections.OrderedDict(sorted(charFreqs.items()))

    s = '{\n' + \
    '            "textLength":{"withSpaces":' + str(len(text)) + ',"withoutSpaces":' + str(len(text) - spacesNum) + '},\n' + \
    '            "wordCount":' + str(wordsNum) + ',\n' + \
    '            "characterCount":['

    count = 0
    for item in od.items():
        if count != 0:
            s = s + ','
        s = s + '{"' + item[0] + '":' + str(item[1]) + '}'
        count = count + 1 

    s = s + ']\n' + '}'

    return s
