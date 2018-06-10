import matplotlib.pyplot as plt
import rgblend

from matplotlib.collections import PolyCollection
import numpy as np



def tribar(figsize = [5,5], xl = 1, d =10):
    """
    Return figure object that contains a vectorized triangle

    :param figsize:
    :param xl: length of triangle side
    :param d: number of discretizations along triangle side
    :return: figure object
    """

    tris, xyc = rgblend.triangles(xl, d)

    fig = plt.figure(figsize=figsize)

    ax = fig.add_axes([0, 0, 1, 1])
    pc = PolyCollection(tris, closed=True)

    # Edge of triangles
    edge = xl * np.array([[-0.5, 0], [0.5, 0], [0, np.sqrt(.75)], [-0.5, 0]])

    rgba = np.vstack([rgblend.xy2rgbd(xyc, 1).T, np.ones(len(xyc))]).T
    pc.set_facecolors(rgba)

    ax.add_collection(pc)

    plt.plot(edge[:, 0], edge[:, 1], 'k-', lw=0.5)
    for loc in ['top', 'bottom', 'left', 'right']:
        ax.spines[loc].set_visible(False)
    plt.xlim([-0.5, .5])
    plt.ylim([0, np.sqrt(.75)])
    plt.gca().set_aspect('equal')

    return fig