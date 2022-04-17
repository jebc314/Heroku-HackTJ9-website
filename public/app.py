from flask import Flask, render_template,request
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/puzzle', methods=["GET"])
def puzzle():
    output = {
        'difficulty':request.args.get('difficulty'),
        'piecescount':request.args.get('piecescount')
    }
    return json.dumps(output)