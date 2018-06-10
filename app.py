from flask import Flask, render_template, jsonify, request
from PIL import Image
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import rgblend


app = Flask(__name__)


@app.route('/')
def index_page():
    dictionary = {'image1': image1,'image2': image2,'image3': image3,'result': '/' + imageresult, 'ternary': '/' + triangle}
    return render_template('index.html', content=dictionary)


@app.route('/API', methods = ['GET'])
def api():
    if request.method == 'GET':

        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        width = int(request.args.get('width'))
        height = int(request.args.get('height'))

        return jsonify({'red': get_value(x, y, width, height, data1), 'blue': get_value(x, y, width, height, data2), 'green': get_value(x, y, width, height, data3)})
    return jsonify({})


def get_value(x, y, width, height, data):
    mx = round(data.shape[0] * x / width)
    my = round(data.shape[1] * y / height)

    return {'value': data[mx, my], 'min': np.amin(data), 'max': np.amax(data)}


def create_image(data, name):
    dim = data.shape[::-1]
    f = data.flatten()
    array = ((f - np.min(f)) / (np.max(f) - np.min(f)) * 255).astype(int)
    rgb = [(i,)*3 for i in array]

    img = Image.new('RGB', dim)
    img.putdata(rgb)
    img.save(name)

    return '/' + name



if __name__ == '__main__':
    data1 = Image.open("test_data/img1_lowres.jpg").convert('L')
    data1 = np.array(data1) / 255
    data2 = Image.open("test_data/img2_lowres.jpg").convert('L')
    data2 = np.array(data2) / 255
    data3 = Image.open("test_data/img3_lowres.jpg").convert('L')
    data3 = np.array(data3) / 255

    # data1 = xr.open_dataarray('test_data/horizon1.nc').values
    # data2 = xr.open_dataarray('test_data/horizon2.nc').values
    # data3 = xr.open_dataarray('test_data/horizon3.nc').values

    image1 = create_image(data1, 'static/images/horizon1.png')
    image2 = create_image(data2, 'static/images/horizon2.png')
    image3 = create_image(data3, 'static/images/horizon3.png')

    prop = rgblend.normalize3arrays(data1.ravel(), data2.ravel(), data3.ravel())

    xy, rgbd = rgblend.transfer(prop)

    # convert values to 0 - 255 int8 format
    rgbi = (rgbd * 255).astype(int)
    rgbi = [tuple(c) for c in rgbi]

    imageresult = 'static/images/result.png'
    img = Image.new('RGB', data1.shape[::-1])
    img.putdata(rgbi)
    img.save(imageresult)

    triangle = 'static/images/triangle.png'
    fig = plt.figure()
    plt.scatter(xy[:, 0], xy[:, 1], c=rgbd, zorder=10)
    plt.plot([-.5, 0.5, 0, -.5], [0, 0, np.sqrt(1.25), 0], c='black', zorder=5)
    plt.fill([-.5, 0.5, 0, -.5], [0, 0, np.sqrt(1.25), 0], c='w', zorder=0)
    plt.axis('off')

    fig.savefig(triangle, bbox_inches='tight', transparent=True)

    app.run()