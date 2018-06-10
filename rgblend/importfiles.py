import os
import numpy as np
import PIL.Image as image



def imgToGrey(img, flip = False):
    img = img.convert('L')
    arr = np.asarray(img)
    if flip:
        arr = 255 - arr
    return arr[::-1][:,::-1]


def import3images(fin1, fin2, fin3):
    """
    Function for importing three image files (Red Green Blue), then greyscaling them, then returning 1D arrays.
    :param fin1: String filename
    :param fin2: String filename
    :param fin3: String filename
    :return arrs[0], arrs[1], arrs[2]: Array representation of input images 
    """

    fins = [fin1, fin2, fin3]


    def importfile(fin):
        if not os.path.isfile(fin): raise ValueError('File does not exist: %s' %fin)
        img = image.open(fin)
        img.rotate(180)
        return img



    imgs = []
    for fin in [fin1, fin2, fin3]:
        img = importfile(fin)
        imgs.append(img)

    return imgs