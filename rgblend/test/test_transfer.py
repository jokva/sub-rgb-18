import pytest
import rgblend.transfer as trans
import numpy as np

def test_normalized_sum():
    random_rgb = np.random.randn(30,3)

    with pytest.raises(ValueError):
        trans.transfer(random_rgb)

def test_dimensions():
    dim3 = np.random.randn(30,2,3)

    with pytest.raises(ValueError):
        trans.transfer(dim3)

    # tests squeezing as well
    col2 = np.random.randn(30,2,1)

    with pytest.raises(ValueError):
        trans.transfer(col2)

def test_within_triangle():
    r, g, b = np.meshgrid(np.linspace(0.1, 1, 10),
                          np.linspace(0.1, 1, 10),
                          np.linspace(0.1, 1, 10))
    rgbun = np.vstack([c.ravel() for c in [r, g, b]]).T
    rgbun = rgbun[~(np.sum(rgbun, axis=1) < 1e-9), :]
    rgbn = (rgbun.T / np.sum(rgbun, axis=1)).T

    xl = 1
    xy, rgbd =trans.transfer(rgbn, xl=xl)

    assert np.all(0 <= xy[:,1])
    assert np.all(xy[:, 1] <= 1)

    assert np.all(-xl / 2 <= xy[:, 0])
    assert np.all(xy[:, 0] <= xl / 2)






