from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return 'This is My Page!'

if __name__ == '__main__':
   app.run('127.0.0.1',port=5000,debug=True)