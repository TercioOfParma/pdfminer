#from distutils.core import setup
from setuptools import setup
from pdfminer import __version__
import sys

requires = ['six', 'pycryptodome']
if sys.version_info >= (3, 0):
    requires.append('chardet')

setup(
    name='pdfminer.six-mgh',
    version=__version__,
    install_requires=requires,
    description='PDF parser and analyzer',
    long_description='''PDFMiner.six-mgh is a tool for extracting information from PDF documents.
Fork using six for Python 2+3 compatibility maintained by the Monumenta Germaniae Historica.
Unlike other PDF-related tools, it focuses entirely on getting
and analyzing text data. PDFMiner allows to obtain
the exact location of texts in a page, as well as
other information such as fonts or lines.
It includes a PDF converter that can transform PDF files
into other text formats (such as HTML). It has an extensible
PDF parser that can be used for other purposes instead of text analysis.''',
    license='MIT/X',
    author='Yusuke Shinyama + Philippe Guglielmetti',
    author_email='pdfminer@goulu.net',
    maintainer='Clemens Radl',
    maintainer_email='clemens.radl@mgh.de',
    url='http://www.mgh.de/soft/pdfminer-six-mgh',
    packages=[
    'pdfminer',
    ],
    package_data={
    'pdfminer': ['cmap/*.pickle.gz']
    },
    scripts=[
    'tools/pdf2txt.py',
    'tools/dumppdf.py',
    'tools/latin2ascii.py',
    ],
    keywords=['pdf parser', 'pdf converter', 'layout analysis', 'text mining'],
    classifiers=[
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Topic :: Text Processing',
    ],
    )
