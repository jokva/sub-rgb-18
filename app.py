from flask import Flask, render_template, jsonify, request
import numpy as np
import matplotlib.pyplot as plt
import requests
import pandas as pd
import holoviews as hv
hv.extension('bokeh')

app = Flask(__name__)


@app.route('/')
def index_page():
    dictionary = {'image1': '/static/myfig.png', 'image2': '/static/myfig.png', 'image2': '/static/myfig.png'}
    return render_template('index.html', content=dictionary)


if __name__ == '__main__':
    app.run()