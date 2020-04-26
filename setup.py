import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="verifyhash", # Replace with your own username
    version="0.1",
    author="Yan Zaripov",
    author_email="yan.zaripov@gmail.com",
    description="Quick verification of some files with verified source hashes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonnyzar/verifyhash/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)