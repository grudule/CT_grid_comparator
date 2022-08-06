from setuptools import setup, find_packages

setup(
    name="dose_comp",
    version="1.0.0",
    author="Alexandre Sagona",
    author_email="alexandre.sagona.1@ulaval.ca",
    description="Quick Analysis for numpy array for dose map",
    url="https://github.com/grudule/dose_comp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
)
