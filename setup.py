from platform import system
import setuptools

dependencies = ['playsound']

system = system()

if system == 'Darwin':
    dependencies.append('PyObjC')
elif system == 'Windows':
    dependencies.append('windows-curses')
else:
    dependencies.append('PyGObject')

del system

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Terminal-Apple-Season",
    version="1.2.2",
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
    include_package_data=True,
    install_requires=dependencies
)
