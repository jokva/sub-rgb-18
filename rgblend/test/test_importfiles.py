import pytest
from rgblend import import3images
import numpy as np


def test_images_import():
	
	with pytest.raises(ValueError):
		import3images("", "", "fin3")

	a1, a2, a3 = import3images('test_data/img1.jpg',
		                       'test_data/img2.jpg',
		                       'test_data/img3.jpg')

	assert isinstance(a1, np.ndarray)
	assert a1.shape == (9144576,)