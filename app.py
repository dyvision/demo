from flask import *
from dotenv import load_dotenv
import os

load_dotenv()

username = os.environ['username']
password = os.environ['pass']


app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
    return "<h1>hello {}</h1>".format(username)

@app.route('/test')
def test():
    final = 14 + int(request.args['number'])
    return str(final)
