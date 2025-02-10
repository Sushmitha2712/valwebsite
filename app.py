print("Starting Flask app...")
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/surprise', methods=['POST'])
def surprise():
    return render_template('surprise.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
