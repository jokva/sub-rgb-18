import numpy as np
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb


def transfer(rgb, xl =1):

    """
    This function is called on a 3 normalized arrays representing r,g,b
    of n points and shape (n,) in a list or tuple.

    In the triangle red will be in bottom left, green on top and blue on the
    bottom right


    :param rgb: np.ndarray with columns defining rgb, which should add up to one
    :param xl: the length of the lower axis
    :return xy: np.ndarray of xy coordinates in 2 columns (n,2)
    :return rgb_display: np.ndarray of rgb values in 3 columns (n,3)
    """

    rgb = np.asarray([np.squeeze(c) for c in rgb]).T

    if np.ndim(rgb) != 2:
        raise ValueError('Dimensions need to be 2')
    nm = np.shape(rgb)

    if nm[1] != 3:
        raise ValueError('rgb needs to have 3 columns')

    if np.any(np.abs(np.sum(rgb, axis=1)-1) > 1e-4):
        raise ValueError('rbg rows do not add up to one')

    # height of triangle
    trih = xl * np.sqrt(.75)

    # y-coordinate (towards green)
    y = trih*rgb[:,1]

    x = .5*(rgb[:,1] + xl*rgb[:,2]*2 -1)

    xy = np.vstack([x,y]).T

    hsv = rgb_to_hsv(rgb)
    hsv[:,2] =1
    rgb_display = hsv_to_rgb(hsv)


    return xy, rgb_display


def xy2rgbd(xy, xl):

    trih = xl * np.sqrt(.75)
    g = xy[:,1]/trih
    b = (xy[:,0]*2 -g +1)/xl/2
    r = 1 - g - b

    rgbd = np.vstack([r,g,b]).T

    return rgbd





