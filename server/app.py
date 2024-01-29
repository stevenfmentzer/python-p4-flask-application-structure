#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

@app.route('/print/<string:string>')
def print_string(string): 
    if isinstance(string, str):
        return f'<p>{string}</p>'
    else: 
        "Invalid parameter. Please provide a string."

@app.route('/count/<int:num>')
def count(num): 
    if isinstance(num, int):
        numbers = list(range(1, num + 1))
        numbers_str = '\n'.join(map(str, numbers))
        return numbers_str
    else: 
        return "Invalid parameter. Please provide an integer."

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        if operation == '+':
            solution = num1 + num2
            return f'<p>{solution}</p>'
        elif operation == '-':
            solution = num1 - num2
            return f'<p>{solution}</p>'
        elif operation == '*':
            solution = num1 * num2
            return f'<p>{solution}</p>'
        elif operation == 'div':
            solution = num1 / num2
            return f'<p>{solution}</p>'
        elif operation == '%':
            solution = num1 % num2
            return f'<p>{solution}</p>'
        else:
            return "Invlaid Operatior. Please choose from: '+', '-', '*', '%', 'div'"
    else:
        return "Invalid parameter. Please provide an integer."

if __name__ == '__main__':
    app.run(port=5555, debug=True)