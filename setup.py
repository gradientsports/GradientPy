from setuptools import setup, find_packages

setup(
    name="gradientpy",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "pandas>=2.0.0",
        "numpy>=1.23.0",
        "python-dotenv>=0.20.0",
    ],
    author="Gradient Sports",
    description="Python library for accessing the Gradient Sports REST API",
    url="https://github.com/gradientsports/GradientPy",
)