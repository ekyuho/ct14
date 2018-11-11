from flask import Flask, request
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    with open("log.txt", "a") as f:
        dstr = datetime.datetime.now()
        f.write("%s, " % (dstr))
        str = ""
        for p in request.args:
            str += "[%s:%s],  " % (p, request.args[p])
            f.write(str)
        f.write("\n");
        if str == "": str = "no parameters"
        print('/', str, flush=True)
    return 'I got: ' + str

@app.route('/cakes')
def cakes():
    print("/cakes", flush=True)
    return 'Yummy cakes!'

print("Waiting at port 5000")
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
