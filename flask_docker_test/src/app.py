from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    print("Inside hello world fun")
    return render_template('index.html')

if __name__ == '__main__':
    print("Inside main")
    app.run(host ='0.0.0.0', port = 5001, debug = True)