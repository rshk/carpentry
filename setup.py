from setuptools import setup, find_packages

version = '0.1-beta'

install_requires = []

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-pep8',
]


setup(
    name='carpentry',
    version=version,
    packages=find_packages(),
    url='http://rshk.github.io/carpentry',
    license='BSD License',
    author='Samuele Santi',
    author_email='redshadow@hackzine.org',
    description='',
    long_description='',
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='tests',
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.7",
    ],
    package_data={'': ['README.md', 'LICENSE']})
