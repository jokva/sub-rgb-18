import argparse
import matplotlib.pyplot as plt

from .plotting import tribar, rgblend
from .importfiles import import3images

def img3():
    parser = argparse.ArgumentParser( description = 'Blend some images')
    parser.add_argument('images', metavar = 'img', nargs = 3)
    parser.add_argument('--flip', action = 'store_const', const = True,
                        default = False)

    args = parser.parse_args()

    imgs = import3images(*args.images)
    rgblend(*imgs, flip=args.flip)
    plt.show()
