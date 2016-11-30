"""
Use setup tools to setup nightmare as a standard python module
"""
from setuptools import setup, find_packages


setup(
    name="myProject",
    version="0.0.1",
    description="practice on behave + selenium",
    url="https://github.com/jessicawjr/myProject",
    packages=find_packages(),
    test_suite="tests",
    entry_points={
        "console_scripts": [
            "baidu=baidu.cli:main",
        ]
    },
)
