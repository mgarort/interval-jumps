import setuptools

setuptools.setup(
    name='jumps',
    version='0.0.1',
    author='Miguel Garcia-Ortegon',
    description='A package to calculate, starting from a note and an interval, what is the final note.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_packages(where=''),
    python_requires='>=3.6',
)

