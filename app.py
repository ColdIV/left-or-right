from flask import Flask, render_template
import os
import sys
from waitress import serve
from random import randrange
import json

from Rank import Rank

# Change secret and port
SECRET='CHANGE YOUR SECRET'
PORT=80

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET

@app.route('/')
@app.route("/vs")
@app.route("/vs/<won>/<lost>")
def index(won = -1, lost = -1):
    if won != -1 and lost != -1:
        tmp1 = Rank(-1, data["data"][won]["points"])
        tmp2 = Rank(-1, data["data"][lost]["points"])
        tmp1Points = tmp1.vs(tmp2, 1, False)
        tmp2Points = tmp2.vs(tmp1, 0, False)
        data["data"][won]["points"] = tmp1Points
        data["data"][lost]["points"] = tmp2Points
        with open('./json/data.json', 'w') as outfile:
            json.dump(data, outfile)
    
    a = randrange(len(data["data"]))
    b = randrange(len(data["data"]))
    while (a == b):
        b = randrange(len(data["data"]))

    aPath = data["data"][str(a)]['path']
    aID = str(a)
    bPath = data["data"][str(b)]['path']
    bID = str(b)
    
    return render_template('versus.html', aPath=aPath, bPath=bPath, aID=aID, bID=bID, active='versus')

@app.route("/leaderboard")
def leaderboard():
    tmp = []
    for i in data["data"]:
        tmp.append({'points': data["data"][i]["points"], 'id': int(i)})
    tmp.sort(key = lambda x: x["points"], reverse = True)
    
    leaderboard = tmp
    d = data["data"]
    
    ldb = []
    for entry in leaderboard:
        ldb.append({'path': d[str(entry["id"])]['path'], 'points': d[str(entry["id"])]["points"]})
    
    return render_template('leaderboard.html', ldb=ldb, active='leaderboard')

if __name__ == '__main__':
    if os.path.isfile('json/data.json'):
        with open('json/data.json') as json_file:
            data = json.load(json_file)
    else:
        print ("loading images...")
        data = {}
        data["data"] = {}

        i = 0
        for filename in os.listdir('./static/images'):
            tmp = {}
            tmp["path"] = '/images/' + filename
            tmp["points"] = 1200
            
            data["data"][i] = {}
            data["data"][i] = tmp
            i += 1

        with open('./json/data.json', 'w') as outfile:
            json.dump(data, outfile)
        print ("images loaded")


    if len(sys.argv) >= 2 and sys.argv[1] == 'dev':
        app.run(debug=True)
    else:
        serve(app, host='0.0.0.0', port=PORT)