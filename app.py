from flask import Flask, request, jsonify, render_template, redirect
import json
import logging
import folium
from folium import plugins
import time, os, uuid

app = Flask(__name__)


@app.route("/show", methods=['post'])
def show():
    if not request.data:
        return 'fail'
    lnglatStr = request.data.decode('utf-8')
    print(lnglatStr)
    lngLatArr = json.loads(lnglatStr)
    print(lngLatArr)
    arr = []
    for i in lngLatArr:
        lnglat = i['lng'], i['lat']
        arr.append(lnglat)
    print(arr)
    html_file = displaygeom(lines=arr, points=arr)
    logging.info(html_file)
    return html_file


@app.route('/<file>')
def to_show_line(file):
    return render_template(file)


@app.route('/displaygeom')
def displaygeom():
    arr = [(113.54, 34.7), (113.54, 34.75), (113.55, 34.85)]
    html_file = displaygeom(lines=arr, points=arr)
    return render_template(html_file)


def displaygeom(lines, points):
    lines = [_[::-1] for _ in lines]
    num = len(lines)
    center_x = sum([_[0] for _ in lines]) / num
    center_y = sum([_[1] for _ in lines]) / num

    m = folium.Map(location=[center_x, center_y],
                   zoom_start=14,
                   width='100%',
                   height='100%',
                   zoom_control='False',
                   tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}&ltype=6',
                   attr='AutoNavi')
    # folium.PolyLine(locations=points, color='green').add_to(m)
    folium.plugins.AntPath(lines, dash_array=[20, 25]).add_to(m)

    points = [_[::-1] for _ in points]
    for p in points:
        folium.Marker(p).add_to(m)
    filename = "{}_{}.html".format("test", str(uuid.uuid1())[:8])
    logging.info("filename" + str(filename))
    outfile = "./templates/" + str(filename)
    logging.warning(f'out_file:{outfile}')
    m.save(outfile)
    return filename


@app.route("/map", methods=['post'])
def getLngLat():
    if not request.data:
        return 'fail'
    lnglat = request.data.decode('utf-8')
    print(lnglat)
    return 'success'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
