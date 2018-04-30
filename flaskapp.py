from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello from Flask!'

@app.route('/time')
def get_time():
    return time.ctime()

if __name__ == '__main__':
  app.run()