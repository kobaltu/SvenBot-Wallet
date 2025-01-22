from setuptools import setup, find_packages

setup(
    name="svenbot-wallet",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask",
        "cryptography",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'svenbot=src.main:main'
        ]
    }
)
