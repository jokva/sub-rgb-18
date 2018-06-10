import os
import numpy as np

def import3images(fin1, fin2, fin3):
    """
    Function for importing three image files (Red Green Blue), then greyscaling them, then returning 1D arrays.
    :param fin1: String filename
    :param fin2: String filename
    :param fin3: String filename
    :return arrs[0], arrs[1], arrs[2]: Array representation of input images 
    """

    fins = [fin1, fin2, fin3]
  
    def imgToGrey(fin):
        import PIL.Image as image
        if not os.path.isfile(fin): raise ValueError('File does not exist: %s' %fin)
        img = image.open(fin).convert('L')
        return img

    def greyToArray(a):
        arr = np.asarray(a)
        return arr
    
    arrs = []
    for fin in [fin1, fin2, fin3]:
        img = imgToGrey(fin)
        arr = greyToArray(img)
        arrs.append(arr)

    return arrs[0], arrs[1], arrs[2]