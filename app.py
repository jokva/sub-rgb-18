from flask import Flask, render_template, jsonify, request
from PIL import Image
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import rgblend


app = Flask(__name__)


@app.route('/')
def index_page():
    dictionary = {'image1': image1,'image2': image2,'image3': image3,'result': '/' + imageresult,
                  'ternary': '/' + ternary, 'triangle': '/' + triangle}
    return render_template('index.html', content=dictionary)


@app.route('/API', methods = ['GET'])
def api():
    if request.method == 'GET':

        x = int(request.args.get('x'))
        y = int(request.args.get('y'))
        width = int(request.args.get('width'))
        height = int(request.args.get('height'))

        return jsonify({'red': get_value(x, y, width, height, data[0]),
                        'green': get_value(x, y, width, height, data[1]),
                        'blue': get_value(x, y, width, height, data[2])})
    return jsonify({})


def get_value(x, y, width, height, value):
    mx = round(value.shape[1] * x / width)
    my = round(value.shape[0] * y / height)

    return {'value': float(value[my, mx]), 'min': float(np.amin(value)), 'max': float(np.amax(value))}


def create_image(value, name):
    dim = value.shape[::-1]
    f = value.flatten()
    array = ((f - np.min(f)) / (np.max(f) - np.min(f)) * 255).astype(int)
    rgb = [(i,)*3 for i in array]

    img = Image.new('RGB', dim)
    img.putdata(rgb)
    img.save(name)

    return '/' + name


def import_image(name):
    data = Image.open(name).convert('L')
    return np.array(data).astype(float)


def import_netcdf(name):
    return xr.open_dataarray(name).values


if __name__ == '__main__':
    data = rgblend.import3images("test_data/img1_lowres.jpg", "test_data/img2_lowres.jpg", "test_data/img3_lowres.jpg")
    data = rgblend.import3images("test_data/img2_1_contrast_saturation_lowres.jpg", "test_data/img2_2_contrast_saturation_lowres.jpg", "test_data/img2_3_contrast_saturation_lowres.jpg")
    # data = list(map(import_netcdf, ("test_data/horizon1.nc", "test_data/horizon2.nc", "test_data/horizon3.nc")))

    image1 = create_image(data[0], 'static/images/horizon1.png')
    image2 = create_image(data[1], 'static/images/horizon2.png')
    image3 = create_image(data[2], 'static/images/horizon3.png')

    prop = rgblend.normalize3arrays(data[0].ravel(), data[1].ravel(), data[2].ravel())

    xy, rgbd = rgblend.transfer(prop)

    # convert values to 0 - 255 int8 format
    rgbi = (rgbd * 255).astype(int)
    rgbi = [tuple(c) for c in rgbi]

    imageresult = 'static/images/result.png'
    img = Image.new('RGB', data[0].shape[::-1])
    img.putdata(rgbi)
    img.save(imageresult)

    ternary = 'static/images/ternary.png'
    fig = plt.figure()
    plt.scatter(xy[:, 0], xy[:, 1], c=rgbd, zorder=10)
    plt.plot([-.5, 0.5, 0, -.5], [0, 0, np.sqrt(1.25), 0], c='black', zorder=5)
    plt.fill([-.5, 0.5, 0, -.5], [0, 0, np.sqrt(1.25), 0], c='w', zorder=0)
    plt.axis('off')

    fig.savefig(ternary, bbox_inches='tight', transparent=True)

    triangle = 'static/images/triangle.png'
    fig = rgblend.tribar()
    fig.savefig(triangle, bbox_inches='tight', transparent=True)

    app.run()