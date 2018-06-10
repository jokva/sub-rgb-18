import setuptools

setuptools.setup(
    name = 'sub-rgb',
    packages = ['rgblend'],
    install_requires = ['matplotlib', 'numpy',],
    setup_requires = ['setuptools>=28', 'pytest-runner'],
    tests_require = ['pytest'],
    entry_points = {
        'console_scripts' : [
            'imgblend = rgblend:img3',
        ],
    }
)
