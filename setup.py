import os

from setuptools import setup, find_packages

DESCRIPTION = 'Download Landsat 8 images from Amazon S3'
NAME = 'pys3landsat'
SCRIPT = os.path.join('bin', NAME)

version = {}
with open('pyamazonlandsat/version.py') as fp:
    exec(fp.read(), version)

setup(
    name=NAME,
    version=version['__version__'],
    packages=find_packages(exclude=['tests*']),
    url='https://github.com/eamanu/pyamazonlandsat',
    license='MIT',
    author='Emmanuel Arias',
    author_email='eamanu@yaerobi.com',
    description=DESCRIPTION,
    scripts=[SCRIPT],
    install_requires=["requests",
                      "attrs",
                      "bs4"],
    tests_require=[
        "pytest==3.0.7",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Operating System :: Linux",
        "Environment :: Console",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

)
