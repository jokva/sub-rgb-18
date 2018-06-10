import numpy as np


def _triangle_row(r, xl, d):

    # Height of triangles
    ht = xl * np.sqrt(.75) / d

    # Bottom x coordinates
    bd = np.linspace(.5 * xl * (-1 + r / d), .5 * xl * (1 - r / d), d + 1 - r)

    # Upwards facing
    # lower left
    cu0 = list(zip(bd[:-1], np.ones(d) * ht * r))
    # lower right
    cu1 = list(zip(bd[1:], np.ones(d) * ht * r))
    # upper
    cu2 = list(zip((bd[1:] + bd[:-1]) / 2, np.ones(d) * ht * (r + 1)))

    # Collect upwards facing triangles in list of arrays with each of shape (3,2)
    tru = list(map(np.asarray, list(zip(cu0, cu1, cu2))))

    # Collect center coordinates
    xuc = (bd[1:] + bd[:-1]) / 2
    yuc = np.ones(len(xuc)) * (ht * r + ht / 3)
    xyuc = np.vstack([xuc, yuc]).T

    # Downwards facing
    r += 1
    # Upper x coordinates of downwards facing
    bd = np.linspace(.5 * xl * (-1 + r / d), .5 * xl * (1 - r / d), d + 1 - r)
    # upper left
    cd0 = list(zip(bd[:-1], np.ones(d) * ht * r))
    # upper right
    cd1 = list(zip(bd[1:], np.ones(d) * ht * r))
    # lower
    cd2 = list(zip((bd[1:] + bd[:-1]) / 2, np.ones(d) * ht * (r - 1)))

    trd = list(map(np.asarray, list(zip(cd0, cd1, cd2))))

    xdc = (bd[1:] + bd[:-1]) / 2
    ydc = np.ones(len(xdc)) * (ht * (r) + 2 * ht / 3 - ht)
    xydc = np.vstack([xdc, ydc]).T

    # Collect upwards and downwards facing centers
    xyc = np.vstack([xyuc, xydc])

    tr = tru + trd
    return tr, xyc

def triangles(xl, d):
    """
    Compute triangle coordinates

    :param xl: length of triangle side
    :param d: number of discretizations along sides
    :return: list of arrays of triangle coordinates and center coordinates
    """


    tris, xyc = [], []

    for r in range(d):
        trir, xycr =  _triangle_row(r, xl, d)
        tris.append(trir)
        xyc.append(xycr)
    tris = sum(tris,[])
    xyc = np.vstack(xyc)

    return tris, xyc