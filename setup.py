from setuptools import setup, find_packages

import bakulla

try:
    long_description = open("README.md", "r").read()
except IOError:
    long_description = (
        "A simple CLI tool."
    )

setup(
    name="bakulla",
    version=bakulla.__version__,
    author="Leapfrog DevOps Team",
    author_email="devops@lftechnology.com",
    packages=find_packages(),
    description="A simple CLI tool.",
    long_description=long_description,
    py_modules=["bakulla"],
    install_requires=[
    ],
    entry_points="""
        [console_scripts]
        bakulla=bakulla.cli:cli
    """,
    url="https://github.com/darmagedon/bakulla",
)
