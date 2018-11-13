from flask import Flask, request
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return 'name=%s'%(request.args.get('name'))

@app.route('/cakes')
def cakes():
    print("/cakes", flush=True)
    return 'Yummy cakes!'

print("Waiting at port 5000", flush=True)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
