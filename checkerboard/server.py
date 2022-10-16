from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<int:row_num>')
@app.route('/<int:row_num>/<int:col_num>')
def hello_world(row_num=8, col_num=8):
    return render_template('index.html', row_num=row_num, col_num=col_num)

if __name__=="__main__":
    app.run(debug=True) 

