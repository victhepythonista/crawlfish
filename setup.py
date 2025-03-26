 

import setuptools
from setuptools import setup, find_packages

long_description = ""
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="crawlfish",
    version="0.1.2",
    author="Victor Kipkemboi",
    author_email="scriptilapia@gmail.com",
    long_description =long_description,
    long_description_content_type="text/markdown",
    description="""An easy to use web crawling library with handy functions for exploring whole websites or single webpages , dynamic element searching , generic web scraping  and  more . It also has helpful shortcut functions for bs4 , requests and selenium . """,
    url="https://github.com/victhepythonista/crawlfish",
    project_urls={
        "Bug Tracker": "https://github.com/victhepythonista/crawlfish/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires = [
            'art',
            'ascii-magic',
            'openpyxl',
            'selenium' , 
            'requests', 
            'tabulate' ,
            'tldextract',
            'bs4',
            'tqdm',
            ]
    packages=find_packages(),
    python_requires=">=3.6",
 
)