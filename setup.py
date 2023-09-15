from setuptools import find_packages, setup

with open("requirements.txt") as f:
    install_requires = [l.replace('==', '>=') for l in f.read().splitlines()]

setup(
    name="wespeaker",
    version="0.1.0",
    description="Speaker verification.",
    author="WeSpeaker",
    namespace_packages=["wespeaker"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
)
