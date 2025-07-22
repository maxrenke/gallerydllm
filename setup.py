"""Install file for gallerydllm."""
from setuptools import setup, find_packages

setup(
    name="gallerydllm",
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Dependencies here, e.g., 'requests'
    ],
    entry_points={
        "console_scripts": [
            "gallerydllm = gallerydllm.main:main",
        ],
    },
)