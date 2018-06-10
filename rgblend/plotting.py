import matplotlib.pyplot as plt
import rgblend

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
    tris, xyc = rgblend.triangles(xl, d)

    if ax is None:
        fig = plt.figure(figsize=figsize)

        ax = fig.add_axes([.1, .1, .8, .8])
        ret = 'figure'


    pc = PolyCollection(tris, closed=True)

    # Edge of triangles
    edge = xl * np.array([[-0.5, 0], [0.5, 0], [0, np.sqrt(.75)], [-0.5, 0]])

    rgba = np.vstack([rgblend.xy2rgbd(xyc, xl).T, np.ones(len(xyc))]).T
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


def rgblend(a1, a2, a3, figsize=[10, 3], aspect = 'auto'):
    nm = np.shape(a1)

    # Ideally check dimensions
    # ..,but for now NO TIME

    nm = np.shape(a1)

    fig, ax = plt.subplots(2, 3, figsize=figsize)

    sa = [rgblend.normalize.normalizeArray2Range(a.ravel()) for a in [a1,a2,a3]]

    na = rgblend.normalize3arrays_numpy(a1,a2,a3)

    xy, rgbd = rgblend.transfer(na)

    img = np.zeros(nm + (3,))

    for ci, c in enumerate(rgbd.T):
        img[:, :, ci] = np.reshape(c, nm)

    plt.sca(ax[0,0])
    img = plt.imshow(img, aspect=aspect)

    plt.sca(ax[0,1])
    ax[0,1] = rgblend.tribar(ax=ax[0,1])

    ax[0, 1].plot(xy[:, 0], xy[:, 1], 'k.', alpha=0.1)

    plt.sca(ax[1, 0])
    img = plt.imshow(np.reshape(sa[0], nm), aspect=aspect, cmap='Greys_r')

    plt.sca(ax[1, 1])
    img = plt.imshow(np.reshape(sa[1], nm), aspect=aspect, cmap='Greys_r')

    plt.sca(ax[1, 2])
    img = plt.imshow(np.reshape(sa[2], nm), aspect=aspect, cmap='Greys_r')

    for loc in ['top', 'bottom', 'left', 'right']:
        ax[0,2].spines[loc].set_visible(False)

    ax[0, 2].set_xticks([])
    ax[0, 2].set_yticks([])

    return fig
