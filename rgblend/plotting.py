import matplotlib.pyplot as plt

from .normalize import normalize3arrays_numpy
from .transfer import transfer, xy2rgbd
from .triangles import triangles
from .importfiles import imgToGrey

from matplotlib.collections import PolyCollection
import numpy as np

def tribar(figsize = [5,5], xl = 1, d =10, ax = None, labels = ['Red', 'Green', 'Blue']):

    """
    Return figure object that contains a vectorized triangle

    :param figsize:
    :param xl: length of triangle side
    :param d: number of discretizations along triangle side
    :return: figure object
    """
    ret = 'axis'
    tris, xyc = triangles(xl, d)

    if ax is None:
        fig = plt.figure(figsize=figsize)

        ax = fig.add_axes([.1, .1, .8, .8])
        ret = 'figure'


    pc = PolyCollection(tris, closed=True)

    # Edge of triangles
    edge = xl * np.array([[-0.5, 0], [0.5, 0], [0, np.sqrt(.75)], [-0.5, 0]])

    rgba = np.vstack([xy2rgbd(xyc, xl).T, np.ones(len(xyc))]).T
    pc.set_facecolors(rgba)

    ax.add_collection(pc)

    # Hide native yaxis
    plt.yticks([])
    
    # Add labels to corners
    corners = [(-0.5, 0.0), (0.0, np.sqrt(.75)), (0.5, 0.0)]
    valigns = ['top', 'bottom', 'top']
    haligns = ['right', 'center', 'left'] 
    for corner, va, ha, label in zip(corners, valigns, haligns, labels):
        x, y = corner
        plt.text(x, y, label, ha=ha, va=va, fontsize=15)

    plt.plot(edge[:, 0], edge[:, 1], 'k-', lw=0.5)
    for loc in ['top', 'bottom', 'left', 'right']:
        ax.spines[loc].set_visible(False)
    plt.xlim([-0.5 * xl, .5 * xl])
    plt.ylim([0, xl * np.sqrt(.75)])

    ax.set_xticks([])
    ax.set_yticks([])
    plt.gca().set_aspect('equal')
    if ret == 'figure':
        return fig
    else:
        return ax


def rgblend(a1, a2, a3, figsize=[10, 3], aspect = 'auto', flip = False):


    ag1 = imgToGrey(a1,flip=flip)
    ag2 = imgToGrey(a2,flip=flip)
    ag3 = imgToGrey(a3,flip=flip)

    a1 = np.asarray(a1)[::-1][:,::-1]
    a2 = np.asarray(a2)[::-1][:,::-1]
    a3 = np.asarray(a3)[::-1][:,::-1]
    nm = np.shape(a1)

    # Ideally check dimensions
    # ..,but for now NO TIME

    nm = np.shape(ag1)

    fig, ax = plt.subplots(2, 3, figsize=figsize)

    #sa = [normalizeArray2Range(a.ravel()) for a in [a1,a2,a3]]



    na = normalize3arrays_numpy(ag1,ag2,ag3)

    xy, rgbd = transfer(na)

    img = np.zeros(nm + (3,))

    for ci, c in enumerate(rgbd.T):
        img[:, :, ci] = np.reshape(c, nm)

    plt.sca(ax[0,0])
    img = plt.imshow(img, aspect=aspect)
    plt.text(.2, .7, 'Blend', ha='left', va='top', fontsize=15, color='k')

    plt.sca(ax[0,1])
    ax[0,1] = tribar(ax=ax[0,1])

    ax[0, 1].plot(xy[:, 0], xy[:, 1], 'k.', alpha=0.1)

    plt.sca(ax[1, 0])
    img = plt.imshow(a1, aspect=aspect, cmap='Greys_r')
    plt.text(.2, .7, 'Red', ha='left', va='top', fontsize=15, color= 'w')

    plt.sca(ax[1, 1])
    img = plt.imshow(a2, aspect=aspect, cmap='Greys_r')
    plt.text(.2, .7, 'Green', ha='left', va='top', fontsize=15, color='w')

    plt.sca(ax[1, 2])
    img = plt.imshow(a3, aspect=aspect, cmap='Greys_r')
    plt.text(.2, .7, 'Blue', ha='left', va='top', fontsize=15, color='w')

    for loc in ['top', 'bottom', 'left', 'right']:
        ax[0,2].spines[loc].set_visible(False)

    ax[0, 2].set_xticks([])
    ax[0, 2].set_yticks([])

    return fig
