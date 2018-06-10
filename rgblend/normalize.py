import numpy as np


def normalize3arrays_numpy(array1, array2, array3):

    '''
    this methode assume that the 3 arrays have the same size.
    :param array1:
    :param array2:
    :param array3:
    :return: 3 arrays, one for each input after normalization to the range, and proportion computation regarding the three arrays.
    '''

    na1 = normalizeArray2Range(array1)
    na2 = normalizeArray2Range(array2)
    na3 = normalizeArray2Range(array3)
    nasum = na1 + na2 + na3
    n0 = nasum != 0
    na1[n0] = na1[n0]/nasum[n0]
    na2[n0] = na2[n0] / nasum[n0]
    na3[n0] = na3[n0] / nasum[n0]
    na1[~n0] = 1/3
    na2[~n0] = 1/3
    na3[~n0] = 1/3


    return na1, na2, na3


def normalize3arrays(array1, array2, array3):

    '''
    this methode assume that the 3 arrays have the same size.
    :param array1:
    :param array2:
    :param array3:
    :return: 3 arrays, one for each input after normalization to the range, and proportion computation regarding the three arrays.
    '''

    narray1 = normalizeArray2Range(array1)
    narray2 = normalizeArray2Range(array2)
    narray3 = normalizeArray2Range(array3)
    return computeProportion3Arrays(narray1, narray2, narray3)


# compute the normalized version of each array
def normalizeArray2Range(array):
    return (array - np.min(array)) / (np.max(array) - np.min(array))


def computeProportion3Arrays(array1, array2, array3):

    # compute for each index of the 3 arrays the normalized corresponding vector of length 3, store it in 3 arrays
    globallyNormalized1stTable = np.zeros(len(array1))
    globallyNormalized2ndTable = np.zeros(len(array2))
    globallyNormalized3rdTable = np.zeros(len(array3))

    for i in range(0, len(array1)):
        norm = (array1[i] + array2[i] + array3[i])
        if norm == 0:
            globallyNormalized1stTable[i] = 1 / 3.0
            globallyNormalized2ndTable[i] = 1 / 3.0
            globallyNormalized3rdTable[i] = 1 / 3.0
        else:
            globallyNormalized1stTable[i] = array1[i] / norm
            globallyNormalized2ndTable[i] = array2[i] / norm
            globallyNormalized3rdTable[i] = array3[i] / norm

    return globallyNormalized1stTable, globallyNormalized2ndTable, globallyNormalized3rdTable
