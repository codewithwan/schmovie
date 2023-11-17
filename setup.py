from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.0.1'
DESCRIPTION = 'A Python library leveraging the OMDb API to fetch movie details based on user-provided titles. It also offers plot translation from English to Indonesian using googletrans.'

this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / 'README.md').read_text()

# Setting up
setup(
    name="schmovie",
    version=VERSION,
    author="codewithwan",
    author_email="<deezerxstore@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/codewithwan/schmovie',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    keywords=['SCH', 'OMDb'],
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
)
