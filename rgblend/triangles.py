import numpy as np

def coordinates(row, outer_width, resolution):
    """
    The coordintes at which there must be a an inner triangle (bottom) corner
    for a given row

    Parameters
    ----------
    row : int
    outer_width : int
    resolution : int

    Returns
    -------
    coords : numpy.ndarray
    """
    return np.linspace(0.5 * outer_width * (-1 + row / resolution),
                       0.5 * outer_width * ( 1 - row / resolution),
                       resolution + 1 - row)

def upwards(row, outer_width, height, resolution):
    """
    Build a list of coordinate-triplets (i,j,k) for one row of triangles,
    facing upwards::

           k
          / \
         /   \
        i-----j

    Parameters
    ----------
    row : int
        the row to build for, where 0 is the bottom row
    outer_width : int
        the length of the outer triangle's sides
    height : int
        the height of each inner triangle (dictates scale of resulting figure)
    resolution : int
        resolution, or discretisation, the number of triangles along each side
        of the (full) triangle

    Returns
    -------
    coords : iterable of [i], [j], [k] lists, each of (x,y) coordinate lists
    """

    bottom = np.full(shape = resolution, fill_value = height * row)
    top    = np.full(shape = resolution, fill_value = height * (row + 1))

    # the points of triangle corners along the row's bottom line
    coords = coordinates(row, outer_width, resolution)

    left = zip(coords[:-1], bottom)
    right = zip(coords[1:], bottom)
    upper = zip((coords[1:] + coords[:-1]) / 2, top)

    return zip(left, right, upper)

def downwards(row, outer_width, height, resolution):
    """
    Build a list of coordinate-triplets (i,j,k) for one row of triangles,
    facing downwards::

        i-----j
         \   /
          \ /
           k

    Parameters
    ----------
    row : int
        the row to build for, where 0 is the bottom row
    outer_width : int
        the length of the outer triangle's sides
    height : int
        the height of each inner triangle (dictates scale of resulting figure)
    resolution : int
        resolution, or discretisation, the number of triangles along each side
        of the (full) triangle

    Returns
    -------
    coords : iterable of [i], [j], [k] lists, each of (x,y) coordinate lists
    """

    # downwards facing triangles for this row share line with upwards facing
    # coordinates of the next row (up), so this problem reduces to replacing
    # the next row's triangles top coordinate with a lower one
    xs = upwards(row + 1, outer_width, height, resolution)

    def f(x):
        left, right, up = x
        up = (up[0], height * row)
        return left, right, up

    return map(f, xs)

def centers(row, outer_width, height, resolution):
    coords = coordinates(row, outer_width, resolution)
    middles = (coords[1:] + coords[:-1]) / 2

    ups = np.vstack([
        middles,
        np.full(len(coords) - 1, height * row + height / 3)
    ]).T

    coords = coordinates(row + 1, outer_width, resolution)
    middles = (coords[1:] + coords[:-1]) / 2

    downs = np.vstack([
        (coords[1:] + coords[:-1]) / 2,
        np.full(len(coords) - 1, height * (row + 1) + 2 * height / 3 - height)
    ]).T

    return np.vstack([ups, downs])

def triangle_row(r, xl, d):

    resolution = d

    # Height of triangles
    ht = xl * np.sqrt(.75) / resolution

    ups = [np.asarray(x) for x in upwards(r, xl, ht, resolution)]
    downs = [np.asarray(x) for x in downwards(r, xl, ht, resolution)]
    cents = centers(r, xl, ht, resolution)

    return ups + downs, cents

def triangles(length, resolution):
    """
    Compute triangle coordinates

    :param xl: length of triangle side
    :param d: number of discretizations along sides
    :return: list of arrays of triangle coordinates and center coordinates
    """


    tris, xyc = [], []

    for r in range(resolution):
        trir, xycr = triangle_row(r, length, resolution)
        tris.append(trir)
        xyc.append(xycr)
    tris = sum(tris,[])
    xyc = np.vstack(xyc)

    return tris, xyc
