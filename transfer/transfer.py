def transfer(rgb, xl =1):

    """
    This function is called on a normalized rgb array
    of n points and shape (n, 3).

    red will be in bottom left, green on top and blue on the
    bottom right


    :param rgb: np.ndarray with columns defining rgb, which should add up to one
    :param xl: the length of the lower axis
    :return xy: np.ndarray of xy coordinates in 2 columns (n,2)
    :return rgb_display: np.ndarray of rgb values in 3 columns (n,3)
    """

    rgb = np.asarray(rgb)

    rgb = np.squeeze(rgb)

    if np.ndim(rgb) != 2:
        raise ValueError('Dimensions need to be 2')
    nm = np.shape(rgb)

    if nm[1] != 3:
        raise ValueError('rgb needs to have 3 columns')

    if np.any(np.abs(np.sum(rgb, axis=1)-1) > 1e-4):
        raise ValueError('rbg rows do not add up to one')

    # height of triangle
    trih = xl * np.sqrt(1.25)

    # y-coordinate (towards green)
    y = trih*rgb[:,1]

    x = .5*(rgb[:,1] + xl*rgb[:,2]/.5 -1)

    xy = np.vstack([x,y]).T

    hsv = rgb_to_hsv(rgb)
    hsv[:,2] =1
    rgb_display = hsv_to_rgb(hsv)


    return xy, rgb_display

