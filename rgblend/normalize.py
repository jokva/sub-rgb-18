import numpy as np

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
    normalizedArray = np.zeros(len(array))
    for j in range(0, len(array)):
        if (max(array) - min(array)) == 0:
            continue
        normalizedArray[j] = (array[j] - min(array)) / (max(array) - min(array))
    return normalizedArray

def computeProportion3Arrays(array1, array2, array3):

    # compute for each index of the 3 arrays the normalized corresponding vector of length 3, store it in 3 arrays
    globallyNormalized1stTable = np.zeros(len(array1))
    globallyNormalized2ndTable = np.zeros(len(array2))
    globallyNormalized3rdTable = np.zeros(len(array3))

    for i in range(0, len(array1)):
        norm = (array1[i] + array2[i] + array2[i])
        if norm == 0:
            globallyNormalized1stTable[i] = 1 / 3.0
            globallyNormalized2ndTable[i] = 1 / 3.0
            globallyNormalized3rdTable[i] = 1 / 3.0
            continue
        globallyNormalized1stTable[i] = array1[i] / norm
        globallyNormalized2ndTable[i] = array2[i] / norm
        globallyNormalized3rdTable[i] = array3[i] / norm

    return globallyNormalized1stTable, globallyNormalized2ndTable, globallyNormalized3rdTable



# length = 2
# firstTable = [1, 2.0]
# secondTable = [3, 5.0]
# thirdTable = [0, 2.0]
# nFirstTable = np.zeros(length)
# for j in range(0, length):
#     if (max(firstTable)-min(firstTable))== 0:
#         continue
#     nFirstTable[j] = (firstTable[j]-min(firstTable))/(max(firstTable)-min(firstTable))
#
# nSecondTable = np.zeros(length)
# for j in range(0, length):
#    nSecondTable[j] = (secondTable[j]-min(secondTable))/(max(secondTable)-min(secondTable))
#
# nThirdTable = np.zeros(length)
# for j in range(0, length):
#    nThirdTable[j] = (thirdTable[j]-min(thirdTable))/(max(thirdTable)-min(thirdTable))
#
# #compute for each index of the 3 arrays the normalized corresponding vector of length 3, store it in 3 arrays
# globallyNormalized1stTable = np.zeros(length)
# globallyNormalized2ndTable = np.zeros(length)
# globallyNormalized3rdTable = np.zeros(length)
#
# for i in range(0, length):
#    norm = (nFirstTable[i]+nSecondTable[i]+nThirdTable[i])
#    if norm == 0:
#        globallyNormalized1stTable[i] = 1/3.0
#        globallyNormalized2ndTable[i] = 1/3.0
#        globallyNormalized3rdTable[i] = 1/3.0
#        continue
#    globallyNormalized1stTable[i] = nFirstTable[i]/norm
#    globallyNormalized2ndTable[i] = nSecondTable[i]/norm
#    globallyNormalized3rdTable[i] = nThirdTable[i]/norm