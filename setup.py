 

import setuptools
from setuptools import setup, find_packages

long_description = ""
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="crawlfish",
    version="0.1.0",
    author="Victor Kipkemboi",
    author_email="scriptilapia@gmail.com",
    long_description =long_description,
    long_description_content_type="text/markdown",
    description="""An easy to use web crawling library for exploring whole websites and webpages , element searching , handy bs4 related shortcuts , generic web scraping functions  and  more  """,
    url="https://github.com/victhepythonista/crawlfish",
    project_urls={
        "Bug Tracker": "https://github.com/victhepythonista/crawlfish/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    packages=find_packages(),
    python_requires=">=3.6",
 
)