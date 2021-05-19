from setuptools import setup, find_packages
import split_df

setup(
    name='split_df',
    version=split_df.__version__,

    packages=find_packages(),
    entry_points={
        'console_scripts': [
        ]
    }
)