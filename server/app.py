#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:message>')
def print_string(message):
    print(message) 
    return message

# Count Route
@app.route('/count/<int:num>')
def count(num):
    output = ""
    for i in range(num):
        output += f"{i}\n"
    return output

# Math Operation Route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        result = "Invalid operation"

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
