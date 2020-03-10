import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="h5xrd", # Replace with your own username
    version="0.0.1",
    author="Songsheng Tao",
    description="A CLI software to unpack h5 files from the synchrotron source",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/st3107/h5xrd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)