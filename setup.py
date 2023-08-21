# This will help to create our ML project as a package
# Every package in python has a setup.py file -> Example seaborn
# We can install this project as a package into other projects
# We can also deploy it on Python PyPi

from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
name='MachineLearning',
version='0.0.1',
author='Mansi',
author_email='mansij2997@gmal.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)

#install_requires = ['numpy', 'pandas', 'seaborn', 'matplotlib']
# find_packages() will check which folder has __init__.py file and consider that as a package
# -e . in requirements.txt makes sure it directly triggers setup.py everytime we try to install packages from requirements.txt
# 