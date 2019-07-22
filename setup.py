import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Terminal-Apple-Season",
    version="1.0.0",
    author="Arin Khare",
    author_email="arinmkhare@gmail.com",
    description="Apple season game for terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lol-cubes/Terminal-Apple-Season",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
    ],
)