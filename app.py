from flask import Flask, render_template, jsonify, request
import matplotlib.pyplot as plt
import xarray as xr


app = Flask(__name__)


@app.route('/')
def index_page():
    image1 = import_image('test_data/horizon1.nc', 'static/horizon1.png')
    image2 = import_image('test_data/horizon2.nc', 'static/horizon2.png')
    image3 = import_image('test_data/horizon3.nc', 'static/horizon3.png')
    imageresult = import_image('test_data/horizon3.nc', 'static/result.png')


    dictionary = {'image1': image1, 'image2': image2, 'image3': image3, 'result': imageresult}
    return render_template('index.html', content=dictionary)


def import_image(file, name):
    f = xr.open_dataarray(file)
    fig = plt.figure()
    plt.imshow(f.values)
    fig.savefig(name)
    return '/' + name


if __name__ == '__main__':
    app.run()