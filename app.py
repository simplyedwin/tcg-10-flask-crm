from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)
database = {}
with open('customers.json') as file:
    database = json.load(file)
print(database)

@app.route('/')
def home():
    return render_template('home.template.html')


@app.route('/customer')
def about():
    return render_template('customer.template.html',db=database)


@app.route('/lucky')
def luckyno():
    num = random.randint(1000, 9999)
    return 'Your lucky number is {}'.format(num)


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
    # app.run(host='localhost', port=8080, debug=True)
