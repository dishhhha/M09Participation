from setuptools import setup, find_packages

setup(
    name='M09',
    version='1.0.0',
    url='https://github.com/dishhhha/M09',
    author='Disha Dubey',
    author_email='dishadubey@gmail.com',
    description='A single function package',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)