from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    x = ""
    for i in range (10):
        x+=str(random.randrange(10))+"<hr>"
    return 'Hello World!'+x



if __name__ == '__main__':
    app.run()
