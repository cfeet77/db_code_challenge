import requests
import json

url = 'https://guarded-springs-51765.herokuapp.com/analyze'

def testStep(verdict, myjson, lenWithSpaces, lenWithoutSpaces, wordCount, expectedCharFreq):
    
    x = requests.post(url, json = myjson)
    
    #print the response text:
    
    print(x.text)
    
    y = json.loads(x.text)
    
    if y['textLength']['withSpaces'] != lenWithSpaces:
        print "test 1 failed"
        verdict = "fail"
    
    if y['textLength']['withoutSpaces'] != lenWithoutSpaces:
        print "test 2 failed"
        verdict = "fail"
    
    if y['wordCount'] != wordCount:
        print "test 3 failed"
        verdict = "fail"
    
    count = 0
    for item in expectedCharFreq:
        actualItem = y['characterCount'][count]
        for subItem in item.items():
            expChar = subItem[0]
            expFreq = subItem[1]
            if not expChar in actualItem:
                print 'test 4a failed: expChar = ' + expChar + ', expFreq = ' + str(expFreq) + ', no matching key found'
            elif actualItem[expChar] != expFreq:
                print 'test 4b failed: expChar = ' + expChar + ', expFreq = ' + str(expFreq) + ', actualFreq = ' + str(actualItem[expChar])
                verdict = "fail"
        count = count + 1
    
verdict = "pass"

testStep(verdict, {'text':'hello 2 times  '}, 15, 11, 3, [{"e":2},{"h":1},{"i":1},{"l":2},{"m":1},{"o":1},{"s":1},{"t":1}])

testStep(verdict, {'text':'more testing 4 coverage'}, 23, 20, 4, \
    [{"a":1},{"c":1},{"e":4},{"g":2},{"i":1},{"m":1},{"n":1},{"o":2},{"r":2},{"s":1},{"t":2},{"v":1}])

print "final verdict: " + verdict
    