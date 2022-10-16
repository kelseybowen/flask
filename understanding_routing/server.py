from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<word>')
def say_word(word):
    return f"Hi {word}!"

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    for i in range(num):
        return f"{word} " * num

if __name__=="__main__":
    app.run(debug=True)