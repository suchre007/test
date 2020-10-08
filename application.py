from flask import Flask, render_template, request
import sys, time
import requests

application = app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/' , methods=['POST'])    
def getvalue():
    quantity=request.form['quantity']
    name=request.form['name']
    ph=request.form['ph']

    response = requests.post('https://lnxq1plv11.execute-api.us-east-1.amazonaws.com/prod/test1000', verify=False)
    print(response)
    return 'Ordered'
    


if __name__ == '__main__':
    app.run(debug=True)
