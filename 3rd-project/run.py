from flask import Flask,request,Response

app=Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>hello there </h1>
'''