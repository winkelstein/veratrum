from setuptools import setup, find_packages


def get_requirements(path: str):
    return [l.strip() for l in open(path, encoding='utf-8')]


setup(
    name="veratrum",
    version="0.1.0",
    author="Andrew Winkelstein",
    author_email="andrew.winkelstein@gmail.com",
    url="https://github.com/winkelstein/veratrum",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
