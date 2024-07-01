from flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return 'Chau mundo'

@app.route('/hello')
def greating():
    return 'Hola Mundo!'

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    num_sum = a + b
    return f"La suma es: {str(num_sum)}"