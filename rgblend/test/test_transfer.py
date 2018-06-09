import pytest
from rgblend import transfer
import numpy as np

def test_normalized_sum():
    random_rgb = [np.random.randn(30) for _ in range(3)]

    with pytest.raises(ValueError):
        transfer(random_rgb)

def test_dimensions():
    dims = [np.random.randn(30) for _ in range(4)]

    with pytest.raises(ValueError):
        transfer(dims)

    # tests squeezing as well
    col2 = [np.random.randn(30,1) for _ in range(2)]

    with pytest.raises(ValueError):
        transfer(col2)

def test_within_triangle():
    r, g, b = np.meshgrid(np.linspace(0.1, 1, 10),
                          np.linspace(0.1, 1, 10),
                          np.linspace(0.1, 1, 10))
    rgbun = np.vstack([c.ravel() for c in [r, g, b]]).T
    rgbun = rgbun[~(np.sum(rgbun, axis=1) < 1e-9), :]
    rgbn = (rgbun.T / np.sum(rgbun, axis=1))

    rgbn = [c for c in rgbn]


    xl = 1
    xy, rgbd =transfer(rgbn, xl=xl)

    assert np.all(0 <= xy[:,1])
    assert np.all(xy[:, 1] <= 1)

    assert np.all(-xl / 2 <= xy[:, 0])
    assert np.all(xy[:, 0] <= xl / 2)






