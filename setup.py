from setuptools import setup, find_packages, find_namespace_packages

__author__ = "Campbell Rankine"

setup(
    name="pytorch-dragon",
    version="0.2.4",  # must match the github version
    author="Campbell Rankine",
    author_email="campbellrankine@gmail.com",
    description="A pytorch integrated Machine Learning / Deep learning utilities library",
    download_url="https://github.com/Campbell-Rankine/pytorch-dragon/archive/refs/tags/PyPI.tar.gz",
    packages=find_packages(where="."),
    install_requires=[  # I get to this in a second
        "setuptools>=61.0",
        "validators",
        "beautifulsoup4",
        "opencv-python",
        "numpy",
        "numba",
        "torch==2.2.2",
        "psutil",
        "typing",
        "datetime",
        "gpytorch",
        "botorch",
        "scikit-learn",
        "scipy",
        "torchvision",
        "matplotlib",
        "requests_html",
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
