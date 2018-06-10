import matplotlib.pyplot as plt
import rgblend

from matplotlib.collections import PolyCollection
import numpy as np



import matplotlib.pyplot as plt
import rgblend

from matplotlib.collections import PolyCollection
import numpy as np



def tribar(figsize = [5,5], xl = 1, d =10, labels = ['Red', 'Green', 'Blue']):
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
    plt.xlim([-0.5*xl, .5*xl])
    plt.ylim([0, xl*np.sqrt(.75)])
    plt.gca().set_aspect('equal')

    return fig