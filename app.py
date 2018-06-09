from flask import Flask, render_template, jsonify, request
from PIL import Image
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import transfer


app = Flask(__name__)


@app.route('/')
def index_page():
    image1 = import_image('test_data/horizon1.nc', 'static/horizon1.png')
    image2 = import_image('test_data/horizon2.nc', 'static/horizon2.png')
    image3 = import_image('test_data/horizon3.nc', 'static/horizon3.png')



    # rgb = transfer.transfer()

    # convert values to 0 - 255 int8 format
    # im = Image.new("RGB", rgb.scale)
    # im.putdata(rgb)
    # im.save("static/result.png")

    imageresult = 'image2' #TODO


    dictionary = {'image1': image1,'image2': image2,'image3': image3,'result': imageresult}
    return render_template('index.html', content=dictionary)


def import_image(file, name):
    data = xr.open_dataarray(file).values
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