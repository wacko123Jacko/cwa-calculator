from setuptools import setup, find_packages

setup(
    name="cwa_calculator",
    version="1.0.0",
    description="A simple Python library for computing a student's Cumulative Weighted Average (CWA).",
    author="MLK",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.8",
)
