import setuptools

setuptools.setup(
    name = 'sub-rgb',
    install_requires = ['matplotlib', 'numpy'],
    setup_requires = ['setuptools>=28', 'pytest-runner'],
    tests_require = ['pytest'],
)
