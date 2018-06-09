from flask import Flask, render_template, jsonify, request
from PIL import Image
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import rgblend


app = Flask(__name__)


@app.route('/')
def index_page():

    data1 = xr.open_dataarray('test_data/horizon1.nc').values
    data2 = xr.open_dataarray('test_data/horizon2.nc').values
    data3 = xr.open_dataarray('test_data/horizon3.nc').values

    image1 = create_image(data1, 'static/horizon1.png')
    image2 = create_image(data2, 'static/horizon2.png')
    image3 = create_image(data3, 'static/horizon3.png')

    prop = rgblend.normalize3arrays(data1.ravel(), data2.ravel(), data3.ravel())

    xy, rgbd = rgblend.transfer(prop)

    #rgbd = np.random.randn(data1.shape[0] * data1.shape[1], 3)

    # convert values to 0 - 255 int8 format
    rgbi = (rgbd * 255).astype(int)
    rgbi = [tuple(c) for c in rgbi]

    imageresult = 'static/result.png'
    img = Image.new('RGB', data1.shape[::-1])
    img.putdata(rgbi)
    img.save(imageresult)

    triangle = 'static/triangle.png'
    fig = plt.figure()
    plt.scatter(xy[:, 0], xy[:, 1], c=rgbd)
    fig.savefig('static/triangle.png')


    dictionary = {'image1': image1,'image2': image2,'image3': image3,'result': '/' + imageresult, 'triangle': '/' + triangle}
    return render_template('index.html', content=dictionary)


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
    app.run()