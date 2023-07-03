import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.4'
PACKAGE_NAME = 'pyDolarVenezuela' 
AUTHOR = 'Francisco Griman'
AUTHOR_EMAIL = 'grihardware@gmail.com'
URL = 'https://github.com/fcoagz/pydolarvenezuela'

LICENSE = 'MIT'
DESCRIPTION = 'esta es una librería en python que te permite consultar los precios del dólar en diferentes monitores en Venezuela y el dolar oficial BCV.'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'requests',
      'bs4',
      'beautifulsoup4'
      ]

CLASSIFIERS = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    classifiers=CLASSIFIERS
)