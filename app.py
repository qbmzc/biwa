from flask import Flask, request, jsonify,render_template
import json

app = Flask(__name__)


@app.route("/map", methods=['post'])
def getLngLat():
    if not request.data:
        return 'fail'
    lnglat = request.data.decode('utf-8')
    print(lnglat)
    return 'success'


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
