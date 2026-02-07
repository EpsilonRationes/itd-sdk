from setuptools import setup, find_packages

setup(
    name='itd-sdk',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'requests', 'pydantic'
    ],
    python_requires=">=3.9"
)
