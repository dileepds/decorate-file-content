"""
A setuptools based setup module.

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    # Specifying name of the project. 
    # 
    
    name='print_file', 
   
    # First verion of the project
    version='1.0.0',

    # Description of the project
    description = 'A Python project to print input file in defired format',  
 
    # Author of the package
    author = 'Dileep',


    # specify package directories
    packages = find_packages('src'),

    # Specify the data file to be included

    package_data={
        'src': ['*.py'], 
        'data': ['*.*'],
    },

    include_package_data=True,

)
